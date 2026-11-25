"""Offline structural checks; does not execute examples or contact link targets."""

from __future__ import annotations

import argparse
import re
import unicodedata
from pathlib import Path
from urllib.parse import unquote, urlsplit

import yaml
from markdown_it import MarkdownIt


CONFLICT = re.compile(r"^(?:<{7}|={7}|>{7}|\|{7})(?:\s.*)?$")
IGNORED = {".git", ".venv", "__pycache__", ".worktrees"}


def heading_ids(tokens) -> set[str]:
    used: set[str] = set()
    for index, token in enumerate(tokens):
        if token.type != "heading_open":
            continue
        inline = tokens[index + 1]
        text = "".join(
            child.content
            for child in inline.children or []
            if child.type in {"text", "code_inline", "image"}
        )
        slug = "".join(
            char
            for char in text.lower()
            if char in {"-", "_"} or unicodedata.category(char)[0] not in {"P", "S"}
        ).replace(" ", "-")
        candidate = slug
        suffix = 0
        while candidate in used:
            suffix += 1
            candidate = f"{slug}-{suffix}"
        used.add(candidate)
    return used


def check(root: Path) -> tuple[list[str], int, int]:
    root = root.resolve()
    files = sorted(
        path for path in root.rglob("*.md")
        if not any(part in IGNORED for part in path.relative_to(root).parts)
    )
    parser = MarkdownIt("commonmark")
    errors: list[str] = []
    parsed = {}
    agents = 0
    for path in files:
        name = path.relative_to(root).as_posix()
        text = path.read_text(encoding="utf-8")
        if not text.strip():
            errors.append(f"{name}: empty Markdown file")
        for number, line in enumerate(text.splitlines(), 1):
            if CONFLICT.fullmatch(line):
                errors.append(f"{name}:{number}: unresolved merge conflict marker")
        if path.parent == root / ".github" / "agents" and path.name.endswith(".agent.md"):
            agents += 1
            lines = text.splitlines()
            if not lines or lines[0] != "---" or "---" not in lines[1:]:
                errors.append(f"{name}: missing or unterminated YAML frontmatter")
            else:
                end = lines.index("---", 1)
                try:
                    fields = yaml.safe_load("\n".join(lines[1:end]))
                except yaml.YAMLError as error:
                    errors.append(f"{name}: invalid YAML frontmatter: {error}")
                else:
                    if not isinstance(fields, dict):
                        errors.append(f"{name}: frontmatter must be a mapping")
                    else:
                        for field in ("name", "description"):
                            if not isinstance(fields.get(field), str) or not fields[field].strip():
                                errors.append(f"{name}: nonempty string '{field}' required")
                text = "\n".join(lines[end + 1:])
        parsed[path] = parser.parse(text)

    anchors = {path: heading_ids(tokens) for path, tokens in parsed.items()}
    for path, tokens in parsed.items():
        name = path.relative_to(root).as_posix()
        for token in tokens:
            for child in token.children or []:
                attribute = {"link_open": "href", "image": "src"}.get(child.type)
                if attribute is None:
                    continue
                destination = child.attrGet(attribute)
                if destination is None:
                    continue
                url = urlsplit(destination)
                if url.scheme or url.netloc:
                    continue
                target = (path.parent / unquote(url.path)).resolve() if url.path else path
                if not target.is_relative_to(root):
                    errors.append(f"{name}: local link escapes repository: {destination}")
                elif not target.exists():
                    errors.append(f"{name}: missing link target: {destination}")
                elif url.fragment:
                    fragment = unquote(url.fragment)
                    if target not in anchors:
                        errors.append(f"{name}: cannot check anchor on non-Markdown target: {destination}")
                    elif fragment not in anchors[target]:
                        errors.append(f"{name}: missing heading anchor: {destination}")
    return errors, len(files), agents


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=Path(__file__).resolve().parents[1])
    args = parser.parse_args()
    if not args.root.is_dir():
        parser.error("--root must be an existing directory")
    errors, files, agents = check(args.root)
    for error in errors:
        print(error)
    print(f"Checked {files} Markdown files and {agents} agent headers; {len(errors)} errors.")
    return 1 if errors else 0


if __name__ == "__main__":
    raise SystemExit(main())
