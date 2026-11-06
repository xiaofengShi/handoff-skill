# session-handoff

[简体中文](README.zh-CN.md) · [Website](https://xiaofengShi.github.io/session-handoff/) · [Release](https://github.com/xiaofengShi/session-handoff/releases/tag/v0.1.0)

**Keep the context. Continue the work.**

Turn an ongoing task into a handoff someone can actually use. Bring the decisions, verified state, and next step into a fresh session—or hand the work to a teammate through GitHub.

![session-handoff preview](https://xiaofengShi.github.io/session-handoff//assets/social.png)

## Quick start

```sh
npx skills add xiaofengShi/session-handoff --skill session-handoff
```

Run the command, choose your agent, and ask for a handoff. The CLI installs to the current project by default; add -g for a global installation.

Requires Node.js 22.20+. Prefer no Node dependency? Clone the repository and use the Python installer.

## Use it

### New session

```text
Use $session-handoff to prepare a self-contained continuation prompt for a fresh conversation. Preserve decisions, verified state, authorization scope, and the next action.
```

### New teammate

```text
Use $session-handoff to prepare a handoff for a teammate who cannot access my machine or chat history. Use accessible GitHub files at a fixed commit; include setup, run, and verification commands. Identify any missing dependency.
```

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
git clone https://github.com/xiaofengShi/session-handoff.git
cd session-handoff
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

For local preview, run `python3 -m http.server 8000 --directory docs` and open `http://localhost:8000/`. To edit product copy, edit `site/content.json`; to change presentation, edit `site/index.html` or `site/assets/`, then rebuild. `examples/shared-handoff.md` documents an actual fixed-version checkout and website build.

## Contributions and license

See CONTRIBUTING.md for behavioral scenarios and contribution requirements. The skill and installer are MIT licensed. This is a workflow for an agent to follow; it does not run arbitrary projects by itself.

[CONTRIBUTING.md](CONTRIBUTING.md) · [LICENSE](LICENSE)
