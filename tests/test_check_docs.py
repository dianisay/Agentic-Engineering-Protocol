import tempfile
import unittest
from pathlib import Path

from scripts.check_docs import check


class DocumentChecks(unittest.TestCase):
    def setUp(self):
        self.directory = tempfile.TemporaryDirectory()
        self.addCleanup(self.directory.cleanup)
        self.root = Path(self.directory.name)

    def write(self, name, text):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")

    def test_links_images_references_and_duplicate_headings(self):
        self.write("README.md", "[inline](docs/topic.md#hello-code)\n"
                   "[reference][topic]\n\n[topic]: docs/topic.md#hello-code-1\n"
                   "![image](image.svg)\n[external](https://example.invalid/)\n")
        self.write("docs/topic.md", "# Hello `code`!\n# Hello code!\n")
        self.write("image.svg", "<svg/>")
        self.assertEqual(check(self.root), ([], 2, 0))

    def test_missing_target_and_anchor(self):
        self.write("README.md", "# Here\n[bad](missing.md)\n[anchor](#absent)\n")
        errors, _, _ = check(self.root)
        self.assertEqual(len(errors), 2)
        self.assertTrue(any("missing link target" in error for error in errors))
        self.assertTrue(any("missing heading anchor" in error for error in errors))

    def test_conflicts_are_checked_inside_fences(self):
        for marker in ("<<<<<<< HEAD", "=======", ">>>>>>> main", "||||||| base"):
            with self.subTest(marker=marker):
                self.write("README.md", f"```\n{marker}\n```\n")
                self.assertIn("merge conflict marker", check(self.root)[0][0])

    def test_fenced_links_are_not_checked(self):
        self.write("README.md", "```\n[example](missing.md)\n```\n")
        self.assertEqual(check(self.root)[0], [])

    def test_local_escape_is_rejected(self):
        self.write("README.md", "[outside](../outside.md)\n")
        self.assertIn("escapes repository", check(self.root)[0][0])

    def test_url_encoded_paths_and_unicode_headings(self):
        self.write("README.md", "[topic](a%20b.md#café--next)\n")
        self.write("a b.md", "# Café / Next\n")
        self.assertEqual(check(self.root)[0], [])

    def test_agent_header_is_a_mapping_with_required_strings(self):
        for header in ("", "---\nname: [broken\n---\n", "---\n- item\n---\n",
                       "---\nname: Agent\ndescription: 5\n---\n"):
            with self.subTest(header=header):
                self.write(".github/agents/reader.agent.md", header + "# Reader\n")
                self.assertTrue(check(self.root)[0])
        self.write(".github/agents/reader.agent.md",
                   "---\nname: Reader\ndescription: Reads evidence.\n---\n# Reader\n")
        self.assertEqual(check(self.root), ([], 1, 1))

    def test_empty_files_and_ignored_environments(self):
        self.write("README.md", "")
        self.write(".venv/package/doc.md", "[bad](missing.md)\n")
        errors, files, _ = check(self.root)
        self.assertEqual(files, 1)
        self.assertEqual(errors, ["README.md: empty Markdown file"])


if __name__ == "__main__":
    unittest.main()
