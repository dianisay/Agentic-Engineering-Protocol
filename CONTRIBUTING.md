# Contributing

This repository contains portable instructions, not a hosted service. Before
contributing, establish that you are authorized to share the material and that
the project owner accepts its [MIT license](LICENSE). Never include private
transcripts, credentials, personal paths, customer information, or copyrighted
material without permission.

1. Describe the problem, intended users, threat and privacy boundaries, and
   evidence that the existing protocol does not already solve it.
2. Place each new rule in its authoritative protocol document and link to it;
   avoid duplicating policy across role instructions and templates.
3. Preserve reduced-capability workflows for hosts without session tools.
   Avoid assumptions about language, infrastructure, or project priorities.
4. Test example workflows and relative Markdown links. Parse each custom-agent
   YAML header and check host compatibility; tests must not touch real users'
   work or execute untrusted repository content.
5. Report what you checked, which tool/host versions you used, failures, and
   remaining uncertainty. Clearly distinguish a citation from a verified claim
   and a template example from an executed system.
6. Request review for changes to approvals, session routing, validation,
   persistence, or privacy boundaries. Do not merge or publish without the
   maintainer's explicit authorization.

For research claims, cite original sources and dates, characterize scope and
limitations, and avoid asserting that more agents or fewer tokens guarantee
better results. See [research guidance](docs/research.md).

## Reproducible structural checks

Install Python 3.11 or newer and [uv](https://docs.astral.sh/uv/), then run:

```sh
uv sync --locked
uv run --locked python -m unittest discover -s tests -v
uv run --locked python scripts/check_docs.py
```

The [checker](scripts/check_docs.py) detects merge conflict markers, empty
Markdown files, broken local links and heading anchors, and invalid required
agent YAML fields. It parses CommonMark inline links, images, and resolved
reference links; heading IDs approximate GitHub's punctuation and duplicate
heading rules. Raw HTML links/anchors, undefined reference labels, external
destinations, and renderer-specific extensions are outside its scope.
It never executes examples or contacts external links. The
[workflow](.github/workflows/document-checks.yml) runs the same commands on
pull requests and pushes to `main`.

These are structural checks, not host schema validation, permission checks,
independent protocol acceptance, or an operational agent trial. Report those
separately. The [initial validation report](docs/validation.md) is historical,
not evidence that the current revision passes.
