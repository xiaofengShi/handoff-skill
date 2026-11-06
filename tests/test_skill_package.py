import re
import unittest
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "skills/session-handoff"


class SkillPackageTest(unittest.TestCase):
    def test_installed_package_keeps_license(self):
        self.assertEqual((ROOT / "LICENSE").read_bytes(), (SKILL / "LICENSE").read_bytes())

    def test_references_are_available_inside_the_installed_package(self):
        # These instructions use inline Markdown links, not reference-style links.
        linked = set()
        for source in SKILL.rglob("*.md"):
            for link in re.findall(r"\[[^\]]+\]\(([^\s)]+)\)", source.read_text(encoding="utf-8")):
                url = urlsplit(link)
                if url.scheme or url.netloc or not url.path:
                    continue
                target = (source.parent / unquote(url.path)).resolve()
                self.assertIn(SKILL.resolve(), target.parents, f"Reference leaves installed package: {link}")
                self.assertTrue(target.is_file(), f"{source}: {link}")
                linked.add(target)
        for reference in (SKILL / "references").glob("*.md"):
            self.assertIn(reference.resolve(), linked, f"Unreachable reference: {reference}")
        self.assertIn((SKILL / "assets/handoff-template.html").resolve(), linked)


if __name__ == "__main__":
    unittest.main()
