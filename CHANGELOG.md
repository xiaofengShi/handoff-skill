# Changelog

## Unreleased

- Route generation, scoped edits, read-only review, and resumption before loading format-specific instructions; move sharing details into an on-demand reference. Preserve user-selected sharing channels and distinguish historical authorization from current permission.
- Add a resume example and complete Chinese installation and maintenance instructions through the shared content source.
- Reject incomplete bilingual copy before generating files, escape JSON-LD script delimiters correctly, use explicit UTF-8, and fix the README preview URL.
- Check pull requests before deployment, cover the advertised Python 3.9 baseline and Python 3.12 rendering workflow, and restrict Pages publishing to main after both checks pass.
- Add regression coverage for deterministic builds, links, translation completeness, JSON-LD, package references/licenses, and installer destination protection.

## v0.3.0

- Default both Session and Project deliveries to standalone offline HTML plus the same Markdown audit source; explicit format requests still take priority.
- Include essential context, evidence, commands, and explanations in the document. Embed necessary visuals with captions and text alternatives; rendering must work without network, JavaScript, CDN assets, or companion files.
- Add an offline HTML template, delivery/validation guidance, and a reproducible project example with an inline SVG and text/table alternative.
- Publish the readable example on Pages. Its optional Markdown renderer is a maintenance dependency, not a runtime requirement for Skill users or recipients.

## v0.2.0

- Add explicit Session and Project handoff scopes, independent of local continuation or GitHub sharing.
- Add a project workflow covering goals, architecture, dependencies, capabilities and evidence, operations, prioritized backlog, permissions, and the first maintenance action.
- Follow the current request’s language for generated or edited handoff prose; explicit output-language instructions take precedence. Preserve commands, identifiers, paths, and original logs.
- Add a whole-project handoff example and update the bilingual homepage, documentation, scope comparison, and copyable prompts.
- Rename the repository to `xiaofengShi/handoff-skill`. The installed skill ID and `$session-handoff` invocation remain unchanged. Existing installations are not renamed.

The canonical website is now https://xiaofengshi.github.io/handoff-skill/ (Chinese: https://xiaofengshi.github.io/handoff-skill/zh/). Use the new Pages URL; repository URL redirects do not guarantee redirects for old Pages paths. Existing clones can update their remote with `git remote set-url origin https://github.com/xiaofengShi/handoff-skill.git`.

## v0.1.0

Initial MIT-licensed release with session continuation, GitHub-based sharing, a bilingual website, a Python installer, and a fixed-version runnable handoff example.
