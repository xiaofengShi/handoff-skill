#!/usr/bin/env python3
"""Build bilingual Pages and README views from the same product copy."""
import html
import json
import shutil
from pathlib import Path
from string import Template

ROOT = Path(__file__).resolve().parents[1]


def build():
    data = json.loads((ROOT / "site/content.json").read_text(encoding="utf-8"))
    common = data["common"]
    if set(data["locales"]) != {"en", "zh"}:
        raise ValueError("site/content.json must contain exactly the en and zh locales")
    if set(data["locales"]["en"]) != set(data["locales"]["zh"]):
        raise ValueError("en and zh must have the same content keys")
    for locale, content in data["locales"].items():
        for left, right in (("feature_titles", "feature_texts"), ("faq_q", "faq_a")):
            if len(content[left]) != len(content[right]):
                raise ValueError(f"{locale}: {left} and {right} must have matching lengths")
    site_template = Template((ROOT / "site/index.html").read_text(encoding="utf-8"))
    readme_template = Template((ROOT / "site/readme.md.tmpl").read_text(encoding="utf-8"))
    output = ROOT / "docs"
    output.mkdir(exist_ok=True)
    shutil.copytree(ROOT / "site/assets", output / "assets", dirs_exist_ok=True)
    for locale, content in data["locales"].items():
        values = common | content
        markdown = readme_template.substitute(values)
        (ROOT / ("README.md" if locale == "en" else "README.zh-CN.md")).write_text(markdown, encoding="utf-8")
        escaped = {key: html.escape(value, quote=True) for key, value in values.items() if isinstance(value, str)}
        escaped["headline_html"] = "<br>".join(html.escape(line) for line in content["headline"].splitlines())
        escaped["features"] = "".join(f"<article><h3>{html.escape(title)}</h3><p>{html.escape(text)}</p></article>" for title, text in zip(content["feature_titles"], content["feature_texts"]))
        escaped["prompts"] = "".join(f'<article class="prompt-box"><div class="prompt-top"><span>{html.escape(content["scope_project" if mode == "project" else "mode_" + mode])}</span><button type="button" data-copy="prompt-{mode}">{html.escape(content["copy"])}</button></div><pre id="prompt-{mode}">{html.escape(content["prompt_" + mode])}</pre></article>' for mode in ("local", "share", "project"))
        escaped["faq"] = "".join(f"<details><summary>{html.escape(question)}</summary><p>{html.escape(answer)}</p></details>" for question, answer in zip(content["faq_q"], content["faq_a"]))
        escaped.update(page_url=common["home"] + ("zh/" if locale == "zh" else ""), assets="../assets/" if locale == "zh" else "assets/", local_home="./", other_lang_code="en" if locale == "zh" else "zh-CN")
        escaped["schema"] = json.dumps({"@context": "https://schema.org", "@type": "SoftwareSourceCode", "name": common["name"], "description": content["description"], "codeRepository": common["repo"], "url": escaped["page_url"], "license": common["repo"] + "/blob/main/LICENSE", "version": common["version"], "inLanguage": content["lang"]}, ensure_ascii=False).replace("<", "\\u003c")
        page = output / ("zh/index.html" if locale == "zh" else "index.html")
        page.parent.mkdir(parents=True, exist_ok=True)
        page.write_text(site_template.substitute(escaped), encoding="utf-8")
    examples = output / "examples"
    examples.mkdir(exist_ok=True)
    for suffix in (".md", ".html"):
        shutil.copy2(ROOT / ("examples/project-handoff" + suffix), examples / ("project-handoff" + suffix))
    (output / ".nojekyll").touch()
    (output / "robots.txt").write_text("User-agent: *\nAllow: /\nSitemap: " + common["home"] + "sitemap.xml\n", encoding="utf-8")
    (output / "sitemap.xml").write_text('<?xml version="1.0" encoding="UTF-8"?><urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>' + html.escape(common["home"]) + '</loc></url><url><loc>' + html.escape(common["home"] + 'zh/') + '</loc></url></urlset>\n', encoding="utf-8")
    print("Built docs/, README.md, and README.zh-CN.md")


if __name__ == "__main__":
    build()
