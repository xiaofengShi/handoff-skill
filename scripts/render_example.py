#!/usr/bin/env python3
"""Render this repository's trusted project handoff Markdown as standalone HTML.

Requires Python 3.10+ and requirements-examples.txt. Raw HTML is enabled so the
reviewed inline SVG in the source survives; do not use this as an untrusted HTML
sanitizer or a general-purpose upload converter.
"""
import html
from pathlib import Path
from string import Template

from markdown_it import MarkdownIt

ROOT = Path(__file__).resolve().parents[1]


def render():
    source = ROOT / "examples/project-handoff.md"
    text = source.read_text(encoding="utf-8")
    title = text.splitlines()[0].removeprefix("# ")
    body = MarkdownIt("commonmark", {"html": True, "breaks": False}).enable("table").render(text)
    body = body.replace("<table>", '<div class="table-scroll"><table>').replace("</table>", "</table></div>")
    template = Template((ROOT / "skills/session-handoff/assets/handoff-template.html").read_text(encoding="utf-8"))
    output = template.substitute(language="en", title=html.escape(title, quote=True), body=body)
    source.with_suffix(".html").write_text(output, encoding="utf-8")
    print("Rendered standalone examples/project-handoff.html from Markdown")


if __name__ == "__main__":
    render()
