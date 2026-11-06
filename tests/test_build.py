import contextlib
import importlib.util
import io
import json
import shutil
import tempfile
import unittest
from html.parser import HTMLParser
from pathlib import Path
from unittest.mock import patch
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SPEC = importlib.util.spec_from_file_location("site_build", ROOT / "scripts/build.py")
build = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(build)


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
        self.ids = []
        self.scripts = []
        self.schema = ""
        self.in_schema = False

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if "id" in attrs:
            self.ids.append(attrs["id"])
        for key in ("href", "src"):
            if attrs.get(key):
                self.links.append(attrs[key])
        if tag == "script":
            self.scripts.append(attrs)
            self.in_schema = attrs.get("type") == "application/ld+json"

    def handle_endtag(self, tag):
        if tag == "script":
            self.in_schema = False

    def handle_data(self, data):
        if self.in_schema:
            self.schema += data


class BuildTest(unittest.TestCase):
    def setUp(self):
        self.temporary = tempfile.TemporaryDirectory()
        self.addCleanup(self.temporary.cleanup)
        self.root = Path(self.temporary.name)
        for directory in ("site", "examples"):
            shutil.copytree(ROOT / directory, self.root / directory)
        self.data = json.loads((self.root / "site/content.json").read_text(encoding="utf-8"))

    def run_build(self):
        (self.root / "site/content.json").write_text(json.dumps(self.data, ensure_ascii=False), encoding="utf-8")
        with patch.object(build, "ROOT", self.root), contextlib.redirect_stdout(io.StringIO()):
            build.build()

    def test_json_ld_preserves_text_without_creating_script_elements(self):
        description = '</script><script>alert("example")</script> 中文 & < >'
        for content in self.data["locales"].values():
            content["description"] = description
        self.run_build()
        for name in ("index.html", "zh/index.html"):
            parser = PageParser()
            parser.feed((self.root / "docs" / name).read_text(encoding="utf-8"))
            self.assertEqual(json.loads(parser.schema)["description"], description)
            self.assertEqual(parser.scripts, [{"src": "../assets/app.js" if name.startswith("zh/") else "assets/app.js", "defer": None}, {"type": "application/ld+json"}])

    def test_incomplete_translation_fails_before_writing_output(self):
        cases = (("en", "feature_texts"), ("zh", "faq_a"))
        for locale, key in cases:
            with self.subTest(locale=locale, key=key):
                removed = self.data["locales"][locale][key].pop()
                with self.assertRaisesRegex(ValueError, "matching lengths"):
                    self.run_build()
                self.assertFalse((self.root / "docs").exists())
                self.data["locales"][locale][key].append(removed)
        del self.data["locales"]["zh"]["intro"]
        with self.assertRaisesRegex(ValueError, "same content keys"):
            self.run_build()
        self.assertFalse((self.root / "docs").exists())

    def test_unsupported_locale_is_not_written_over_chinese_readme(self):
        self.data["locales"]["es"] = dict(self.data["locales"]["en"])
        with self.assertRaisesRegex(ValueError, "exactly the en and zh"):
            self.run_build()
        self.assertFalse((self.root / "README.zh-CN.md").exists())

    def test_generated_pages_have_resolvable_local_links(self):
        self.run_build()
        docs = self.root / "docs"
        for path in docs.rglob("*.html"):
            parser = PageParser()
            parser.feed(path.read_text(encoding="utf-8"))
            self.assertEqual(len(parser.ids), len(set(parser.ids)), path)
            for link in parser.links:
                url = urlsplit(link)
                if url.scheme or url.netloc:
                    continue
                target = (path.parent / unquote(url.path)).resolve() if url.path else path
                if target.is_dir():
                    target /= "index.html"
                self.assertTrue(target.is_file(), f"{path}: {link}")
                if url.fragment and target.suffix == ".html":
                    target_parser = PageParser()
                    target_parser.feed(target.read_text(encoding="utf-8"))
                    self.assertIn(unquote(url.fragment), target_parser.ids, f"{path}: {link}")
        image_url = self.data["common"]["home"] + "assets/social.png"
        for name in ("README.md", "README.zh-CN.md"):
            self.assertIn(f"]({image_url})", (self.root / name).read_text(encoding="utf-8"))

    def test_build_is_reproducible_and_matches_committed_views(self):
        self.run_build()
        paths = [self.root / "README.md", self.root / "README.zh-CN.md"]
        paths.extend(path for path in (self.root / "docs").rglob("*") if path.is_file())
        first = {path.relative_to(self.root): path.read_bytes() for path in paths}
        self.run_build()
        for relative, expected in first.items():
            self.assertEqual((self.root / relative).read_bytes(), expected, relative)
            self.assertEqual((ROOT / relative).read_bytes(), expected, f"Stale generated file: {relative}")


if __name__ == "__main__":
    unittest.main()
