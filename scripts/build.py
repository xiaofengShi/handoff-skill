#!/usr/bin/env python3
"""Build bilingual Pages and README views from the same product copy."""
import html
import json
import shutil
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parents[1]


def build():
    data = json.loads((ROOT / "site/content.json").read_text())
    common = data["common"]
    site_template = Template((ROOT / "site/index.html").read_text())
    readme_template = Template((ROOT / "site/readme.md.tmpl").read_text())
    output = ROOT / "docs"
    output.mkdir(exist_ok=True)
    shutil.copytree(ROOT / "site/assets", output / "assets", dirs_exist_ok=True)
    for locale, content in data["locales"].items():
        values = common | content
        markdown = readme_template.substitute(values)
        (ROOT / ("README.md" if locale == "en" else "README.zh-CN.md")).write_text(markdown)
        escaped = {key: html.escape(value, quote=True) for key, value in values.items() if isinstance(value, str)}
        escaped["headline_html"] = "<br>".join(html.escape(line) for line in content["headline"].splitlines())
        escaped["features"] = "".join(f"<article><h3>{html.escape(title)}</h3><p>{html.escape(text)}</p></article>" for title, text in zip(content["feature_titles"], content["feature_texts"]))
        escaped["prompts"] = "".join(f'<article class="prompt-box"><div class="prompt-top"><span>{html.escape(content["mode_" + mode])}</span><button type="button" data-copy="prompt-{mode}">{html.escape(content["copy"])}</button></div><pre id="prompt-{mode}">{html.escape(content["prompt_" + mode])}</pre></article>' for mode in ("local", "share"))
        escaped["faq"] = "".join(f"<details><summary>{html.escape(question)}</summary><p>{html.escape(answer)}</p></details>" for question, answer in zip(content["faq_q"], content["faq_a"]))
        escaped.update(page_url=common["home"] + ("zh/" if locale == "zh" else ""), assets="../assets/" if locale == "zh" else "assets/", local_home="./", other_lang_code="en" if locale == "zh" else "zh-CN")
        escaped["schema"] = json.dumps({"@context": "https://schema.org", "@type": "SoftwareSourceCode", "name": common["name"], "description": content["description"], "codeRepository": common["repo"], "url": escaped["page_url"], "license": common["repo"] + "/blob/main/LICENSE", "version": common["version"], "inLanguage": content["lang"]}, ensure_ascii=False).replace("<", "\u003c")
        page = output / ("zh/index.html" if locale == "zh" else "index.html")
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(site_template.substitute(escaped))
    (output / ".nojekyll").touch()
    (output / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: " + common["home"] + "sitemap.xml\n")
    (output / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>' + common["home"] + '</loc></url><url><loc>' + common["home"] + 'zh/</loc></url></urlset>\n')
    print("Built docs/, README.md, and README.zh-CN.md")


if __name__ == "__main__":
    build()
