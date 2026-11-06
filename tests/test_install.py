import os
import subprocess
import sys
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


class InstallTest(unittest.TestCase):
    def test_install_respects_codex_home_and_preserves_existing(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            environment = dict(os.environ, CODEX_HOME=str(base / "codex"))
            command = [sys.executable, str(ROOT / "scripts/install.py")]
            subprocess.run(command, env=environment, cwd=base, check=True, capture_output=True)
            installed = base / "codex/skills/session-handoff"
            for source in (ROOT / "skills/session-handoff").rglob("*"):
                if source.is_file():
                    self.assertEqual(source.read_bytes(), (installed / source.relative_to(ROOT / "skills/session-handoff")).read_bytes())
            marker = installed / "user-note.txt"
            marker.write_text("keep")
            again = subprocess.run(command, env=environment, cwd=base, capture_output=True, text=True)
            self.assertNotEqual(again.returncode, 0)
            self.assertIn("already exists", again.stderr)
            self.assertEqual(marker.read_text(), "keep")

    def test_symlink_destination_is_not_overwritten(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            destination = base / "skill"
            destination.symlink_to(base / "missing")
            result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"), "--dest", str(destination)], capture_output=True)
            self.assertNotEqual(result.returncode, 0)
            self.assertTrue(destination.is_symlink())

    def test_explicit_destination_takes_precedence_over_codex_home(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            destination = base / "with spaces" / "session-handoff"
            environment = dict(os.environ, CODEX_HOME=str(base / "unused"))
            subprocess.run([sys.executable, str(ROOT / "scripts/install.py"), "--dest", str(destination)], env=environment, cwd=base, check=True, capture_output=True)
            self.assertTrue((destination / "SKILL.md").is_file())
            self.assertFalse((base / "unused").exists())

    def test_existing_file_and_live_symlink_remain_untouched(self):
        with tempfile.TemporaryDirectory() as temporary:
            base = Path(temporary)
            existing = base / "existing"
            existing.write_text("keep", encoding="utf-8")
            link = base / "link"
            link.symlink_to(existing)
            for destination in (existing, link):
                with self.subTest(destination=destination):
                    result = subprocess.run([sys.executable, str(ROOT / "scripts/install.py"), "--dest", str(destination)], capture_output=True)
                    self.assertNotEqual(result.returncode, 0)
                    self.assertEqual(existing.read_text(encoding="utf-8"), "keep")
                    self.assertTrue(link.is_symlink())


if __name__ == "__main__":
    unittest.main()
