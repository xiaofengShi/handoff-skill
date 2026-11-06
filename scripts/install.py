#!/usr/bin/env python3
"""Install the packaged skill without overwriting an existing installation."""
import argparse
import os
import shutil
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--dest", type=Path, help="Exact destination skill directory")
    args = parser.parse_args()
    source = Path(__file__).resolve().parents[1] / "skills" / "session-handoff"
    codex_dir = Path(os.environ.get("CODEX_HOME") or Path.home() / ".codex")
    destination = args.dest or codex_dir / "skills" / "session-handoff"
    if destination.exists() or destination.is_symlink():
        parser.exit(1, f"Destination already exists; inspect and back it up first: {destination}\n")
    destination.parent.mkdir(parents=True, exist_ok=True)
    shutil.copytree(source, destination)
    print(f"Installed: {destination}")


if __name__ == "__main__":
    main()
