# Project handoff: maintain Handoff Skill

**Scope:** Project + GitHub sharing. **Snapshot:** 6 November 2026, commit `0127b54ea88e46d72ac40832b7d2facd62635832`. The recipient can use this guide without the sender’s machine, chat history, or installed Skill.

## Purpose and boundary

Handoff Skill helps an agent prepare Session continuations and whole-project handovers. Both scopes can use a same-machine workspace or accessible GitHub sources. Handoff prose follows the current request’s language unless another output language is explicitly requested. The installed Skill ID is `session-handoff`; the public repository is `handoff-skill`.

This handover covers the Skill package, Python installer, installation tests, bilingual README and website, and GitHub Pages deployment. The project does not supply a backend service, dataset, model, API credential, or the application being handed off by an end user. Do not confuse this example project’s build with proof that an arbitrary user project can run.

## Source and reading order

Public repository: https://github.com/xiaofengShi/handoff-skill. Fixed commit: `0127b54ea88e46d72ac40832b7d2facd62635832`. HTTPS cloning requires no account. A maintainer needs repository write access for authorized pushes or releases, and permission to configure Pages if that is their assigned task; those permissions are not required for the local steps below.

Read the snapshot in this order:

1. [README.md](https://github.com/xiaofengShi/handoff-skill/blob/0127b54ea88e46d72ac40832b7d2facd62635832/README.md) and [CONTRIBUTING.md](https://github.com/xiaofengShi/handoff-skill/blob/0127b54ea88e46d72ac40832b7d2facd62635832/CONTRIBUTING.md) for installation, development, and validation.
2. [SKILL.md](https://github.com/xiaofengShi/handoff-skill/blob/0127b54ea88e46d72ac40832b7d2facd62635832/skills/session-handoff/SKILL.md) and [Project reference](https://github.com/xiaofengShi/handoff-skill/blob/0127b54ea88e46d72ac40832b7d2facd62635832/skills/session-handoff/references/project-handoff.md) for scope, language, evidence, and authorization rules.
3. [Product copy](https://github.com/xiaofengShi/handoff-skill/blob/0127b54ea88e46d72ac40832b7d2facd62635832/site/content.json), [build script](https://github.com/xiaofengShi/handoff-skill/blob/0127b54ea88e46d72ac40832b7d2facd62635832/scripts/build.py), and [Pages workflow](https://github.com/xiaofengShi/handoff-skill/blob/0127b54ea88e46d72ac40832b7d2facd62635832/.github/workflows/pages.yml) for the website and documentation lifecycle.
4. [Changelog](https://github.com/xiaofengShi/handoff-skill/blob/0127b54ea88e46d72ac40832b7d2facd62635832/CHANGELOG.md) for the repository rename and unchanged Skill invocation.

## Structure and main paths

| Location | Responsibility |
| --- | --- |
| `skills/session-handoff/SKILL.md` | Common behavior, Session defaults, Project routing, output language, sharing and continuation |
| `skills/session-handoff/references/project-handoff.md` | Project evidence gathering, overall capabilities, operations, backlog and takeover requirements |
| `skills/session-handoff/agents/openai.yaml` | Codex display metadata and implicit invocation policy |
| `scripts/install.py` | Standard-library installer; refuses existing files/directories and symlink destinations |
| `tests/test_install.py` | Installation behavior checks, including protection of an existing installation |
| `site/content.json` | Shared English/Chinese product copy, URLs, version, prompts and scope comparison |
| `site/index.html`, `site/assets/` | Site template, CSS, interaction code and sharing image |
| `site/readme.md.tmpl` | Template for both READMEs |
| `scripts/build.py` | Generates `docs/`, `README.md` and `README.zh-CN.md` from the source files |
| `docs/` | Generated static site, local assets, robots.txt and sitemap |
| `.github/workflows/pages.yml` | On main push: build, test, require clean generated files, upload and deploy Pages |

Two primary user paths are: installing the Skill and requesting a handoff; and maintaining source copy/templates followed by regeneration and review. Recipients of a generated handoff do not need this Skill installed.

## From an empty directory

Requirements: Git and Python 3.9+. The commands below use macOS/Linux shell syntax. No Python package, external font, private input or credential is required to build, test or preview this project. Skills CLI installation is optional and requires Node.js 22.20+.

Run from a directory without `handoff-project-example`:

```sh
git clone https://github.com/xiaofengShi/handoff-skill.git handoff-project-example
cd handoff-project-example
git checkout --detach 0127b54ea88e46d72ac40832b7d2facd62635832
python3 scripts/build.py
python3 -m unittest discover -s tests
git diff --exit-code
python3 -m http.server 8000 --bind 127.0.0.1 --directory docs
```

Expected: build prints `Built docs/, README.md, and README.zh-CN.md`; two installer tests pass with `OK`; regeneration produces no diff. Open `http://127.0.0.1:8000/` and `/zh/` for English and Chinese. Stop your own preview server with Ctrl+C. If port 8000 is occupied, use a free port; do not stop someone else’s service.

To inspect an actual package installation without replacing an existing Skill, run in a fresh directory with a destination that does not exist:

```sh
python3 scripts/install.py --dest ./review-install/session-handoff
```

The installed folder should contain `SKILL.md`, `LICENSE`, `agents/openai.yaml`, and `references/project-handoff.md`. This installs instructions; it does not execute an application or authorize publication.

## State and evidence

At this snapshot, the package includes Session/Project routing, local/GitHub sharing requirements, and automatic output-language selection. The Project reference covers goals, structure, dependencies, overall state, operations, priorities, permissions and a first executable action. These are workflow instructions, not a deterministic guarantee about every model response.

The automated tests cover installer behavior. They do not prove handoff quality. For behavioral review, use separate current-task and whole-project requests, and test requests whose language differs from the Chinese instruction source. A project share should name unavailable local changes or permissions; a same-machine handoff can reference the actual local workspace. Commands and identifiers should retain their original spelling when prose is translated.

The static website and CI configuration are included in this commit. A successful local build does not establish the currently deployed Pages revision. The live canonical URL is https://xiaofengshi.github.io/handoff-skill/; use GitHub Actions and the live page to check an authorized deployment’s actual result. Old Pages paths are not guaranteed to redirect after the repository rename.

## Maintain and release

- Edit workflow behavior in `SKILL.md` or its Project reference. Update Codex metadata when the visible behavior changes.
- Edit shared copy, version, installation URLs and prompts in `site/content.json`; edit presentation in `site/`. Run `python3 scripts/build.py`, then inspect both READMEs and language pages. Do not hand-edit generated views.
- Keep root and installed-package `LICENSE` copies identical. Preserve third-party attribution if future contributions introduce licensed material.
- Run installer tests and suitable behavioral scenarios. Check mobile overflow, keyboard controls, clipboard feedback, and that core content remains readable without JavaScript after UI changes.
- An authorized push to `main` triggers Pages. Inspect build/deploy logs in GitHub Actions and validate the actual live pages. If a deployment regresses, inspect the failing run and compare with the last known good commit; revert or redeploy only with the current user’s authorization. Keep the working tree’s unrelated changes intact.
- For an authorized release, package the Skill directory with its reference and license, publish a versioned Release and checksum, and verify the public downloads. Never upload local conversations, credentials or private project inputs.

There is no database, persistent server data or long-running project job to transfer for this repository’s static build. Repository code, committed site assets and release artifacts are the relevant recoverable materials. User projects handled by the Skill can have additional runtime and recovery requirements; record those in their own handover.

## First maintenance action, backlog and permissions

Start with the fixed-version checkout, build and tests above. Then inspect the current assigned Issue or requirement before changing behavior. Do not invent a roadmap: the concrete next action from this handoff is to verify the project baseline and report its actual results. No private dependency blocks this local baseline. Installing optional agent hosts and proving their response quality are separate from these installer tests.

Publication, Pages changes, releases, access management and remote rollback require the recipient’s current authorization. The sender’s earlier approvals are historical context, not transferable permissions.

## Starter prompt

```text
Maintain the Handoff Skill project from the fixed repository revision in this handover. Read the project boundaries, Skill rules, Project reference, contribution guide and build/deployment sources. First obtain the snapshot and run the documented build and installation tests in a fresh checkout. Report the verified baseline, any missing dependencies and the first authorized maintenance task. Preserve unrelated changes and do not publish or change access without current authorization.
```

## 中文说明

这份示例移交的是整个 Handoff Skill 项目，包括 Skill 本体、安装器、测试、中英内容源、主页构建和 Pages 发布流程。它按固定版本给出资料阅读顺序、结构、从零运行、证据范围、维护方法、第一项行动和权限条件。接收者无需发送者的机器或聊天记录即可验证基线；后续修改与发布仍遵循接收者当前用户的授权。实际生成的 Project 交接会使用用户请求的语言，本文件是英文交接示例。
