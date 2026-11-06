# Handoff Skill

[简体中文](README.zh-CN.md) · [Website](https://xiaofengshi.github.io/handoff-skill/) · [Release](https://github.com/xiaofengShi/handoff-skill/releases/tag/v0.3.0)

**Keep the context. Continue the work.**

Carry a task into a fresh conversation, or give a new maintainer the context to run and maintain an entire project. Both scopes support local continuation and GitHub sharing, in the language of your request.

The repository is named handoff-skill. The installed skill ID remains session-handoff, so existing $session-handoff requests continue to work.

![Handoff Skill preview](https://xiaofengshi.github.io/handoff-skill//assets/social.png)

## Quick start

```sh
npx skills add xiaofengShi/handoff-skill --skill session-handoff
```

Run the command, choose your agent, and ask for a handoff. The CLI installs to the current project by default; add -g for a global installation.

Requires Node.js 22.20+. Prefer no Node dependency? Clone the repository and use the Python installer.

## Choose the scope. Then the recipient.

A new teammate may need one task or the whole project. The handoff scope and the way you share it are independent.

| Scope | Same machine | GitHub sharing |
| --- | --- | --- |
| Session | Current task, decisions, relevant changes, next action. | Current task at an accessible revision, with inputs and execution steps. |
| Project | Project goals, structure, dependencies, current capabilities, operations, and backlog. | A whole-project guide with accessible sources, fixed versions, setup, verification, and maintenance. |

Session is the default for “handoff this conversation.” Ask for a “project handoff” or “hand over the whole project” to include overall structure and maintenance.

Handoff text follows the language of your current request, unless you explicitly request another language. Commands, identifiers, paths, and original logs stay accurate.

## A handoff you can read on its own.

Both Session and Project handoffs default to a standalone HTML file, with the same Markdown audit source. The essential context, evidence, commands, and explanations stay in the document—even offline and without JavaScript.

Include embedded diagrams or screenshots when they help someone understand the structure, workflow, or current state. Each visual needs a caption and a text alternative. Source code and large inputs remain available through the documented GitHub access requirements.

An explicit request for plain text, Markdown only, another format, or no saved files takes priority.

[Open the standalone project handoff](https://xiaofengshi.github.io/handoff-skill/examples/project-handoff.html) · [Markdown audit source](examples/project-handoff.md)

## Use it

### New session

```text
Use $session-handoff to prepare a self-contained continuation prompt for a fresh conversation. Preserve decisions, verified state, authorization scope, and the next action.
```

### New teammate

```text
Use $session-handoff to prepare a handoff for a teammate who cannot access my machine or chat history. Use accessible GitHub files at a fixed commit; include setup, run, and verification commands. Identify any missing dependency.
```

### Project

```text
Use $session-handoff to hand over this entire project to a new maintainer via GitHub. Cover goals, architecture, dependencies, current capabilities and evidence, operations, backlog, and the first maintenance action. Use accessible sources at fixed revisions; identify missing inputs or permissions.
```

[Open the standalone project handoff](https://xiaofengshi.github.io/handoff-skill/examples/project-handoff.html)

[Read a complete, runnable handoff example](examples/shared-handoff.md)

Illustrative example; repository and version are specified in a real handoff.

```text
Goal
Continue the export feature from a fixed GitHub commit.

Get the work
Repository URL + full commit SHA + relative file paths.

Prepare
Runtime, locked dependencies, inputs, and access requirements.

Run & verify
Exact commands, expected result, and next action.

Open dependency
Recipient must configure their own API credentials.
```

## Manual Codex installation

From a clone of this repository, run the standard-library installer. It respects CODEX_HOME and refuses to overwrite an existing installation.

```sh
git clone https://github.com/xiaofengShi/handoff-skill.git
cd handoff-skill
python3 scripts/install.py
```

Python ≥ 3.9. `python3 scripts/install.py --dest /path/to/skills/session-handoff` installs to a chosen skill directory. Existing directories and symlinks are never overwritten. Back up your old installation before updating. Remove only the installed skill directory to uninstall.

The package follows the SKILL.md format and includes Codex metadata. Other agents’ installation support depends on the host and the [Skills CLI](https://github.com/vercel-labs/skills). Core instructions are currently in Chinese; output follows the user's language. Recipients of a handoff do not need this skill installed. A handoff still requires the project's actual environment, permissions, inputs, and credentials.

## Build and check

The website and these READMEs are generated from site/content.json. No frontend dependency or external font is required.

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests
git diff --check
```

To regenerate the standalone HTML example, use Python 3.10+ with `python3 -m pip install -r requirements-examples.txt`, then run `python3 scripts/render_example.py` before the site build. Skill use, installation, and the site builder do not require this optional example-rendering dependency.

For local preview, run `python3 -m http.server 8000 --directory docs` and open `http://localhost:8000/`. To edit product copy, edit `site/content.json`; to change presentation, edit `site/index.html` or `site/assets/`, then rebuild. `examples/shared-handoff.md` documents an actual fixed-version checkout and website build.

## Contributions and license

See CONTRIBUTING.md for behavioral scenarios and contribution requirements. The skill and installer are MIT licensed. This is a workflow for an agent to follow; it does not run arbitrary projects by itself.

[CONTRIBUTING.md](CONTRIBUTING.md) · [LICENSE](LICENSE)
