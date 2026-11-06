import re
import unittest
from html.parser import HTMLParser
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class ResourceParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.dependencies = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in {"img", "script", "iframe", "audio", "video", "source", "embed", "input"}:
            for key in ("src", "srcset", "poster"):
                if attrs.get(key) and not attrs[key].startswith("data:"):
                    self.dependencies.append((tag, key, attrs[key]))
        if tag in {"image", "use"}:
            for key in ("href", "xlink:href"):
                if attrs.get(key) and not attrs[key].startswith(("data:", "#")):
                    self.dependencies.append((tag, key, attrs[key]))
        if tag == "link" and attrs.get("rel") in {"stylesheet", "preload", "modulepreload"}:
            self.dependencies.append((tag, "href", attrs.get("href")))
        if tag == "object":
            self.dependencies.append((tag, "data", attrs.get("data")))


class ExampleDocumentTest(unittest.TestCase):
    def test_reading_does_not_fetch_companion_or_remote_resources(self):
        document = (ROOT / "examples/project-handoff.html").read_text(encoding="utf-8")
        parser = ResourceParser()
        parser.feed(document)
        self.assertEqual(parser.dependencies, [])
        self.assertNotRegex(document, r"(?i)@import\s")
        for reference in re.findall(r"url\(\s*['\"]?([^)'\"]+)", document):
            self.assertTrue(reference.startswith(("#", "data:")), reference)


if __name__ == "__main__":
    unittest.main()
