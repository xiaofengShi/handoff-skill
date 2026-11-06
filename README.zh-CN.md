# Handoff Skill

[English](README.md) · [Website](https://xiaofengshi.github.io/handoff-skill/) · [Release](https://github.com/xiaofengShi/handoff-skill/releases/tag/v0.3.0)

**保留上下文，让工作继续。**

把当前任务交给新会话，或让新维护者理解、运行并继续维护整个项目。两种范围都支持同机续接与 GitHub 分享，交接内容自动使用你的请求语言。

仓库名称为 handoff-skill，已安装 Skill 的标识仍是 session-handoff，已有 $session-handoff 调用继续有效。

![Handoff Skill preview](https://xiaofengshi.github.io/handoff-skill//assets/social.png)

## 快速开始

```sh
npx skills add xiaofengShi/handoff-skill --skill session-handoff
```

运行命令，选择使用的 Agent，然后提出交接请求。CLI 默认安装到当前项目；加上 -g 可全局安装。

需要 Node.js 22.20 或更新版本。不想依赖 Node？克隆仓库后使用 Python 安装器。

## 先确定交接范围，再确定接收对象。

交给别人接手的，可能是一项任务，也可能是整个项目。交接范围与分享方式是两个独立维度。

| 范围 | 同机续接 | GitHub 分享 |
| --- | --- | --- |
| Session | 当前任务、关键决定、相关改动与下一步。 | 对方可获取的任务版本、输入与执行步骤。 |
| Project | 项目目标、结构、依赖、整体能力、维护方式与待办。 | 完整项目接手说明、固定版本、环境、验证与维护步骤。 |

“交接一下／换个对话继续”默认按 Session 处理；“项目交接／交接整个项目”会覆盖整体结构与维护方式。

交接正文默认跟随用户当前请求的语言；明确指定输出语言时，以指定为准。命令、标识符、路径和原始日志保持准确。

## 一份文件，就能独立阅读。

Session 与 Project 默认都交付独立 HTML，并保留同源 Markdown。必要的背景、证据、命令和操作说明留在文档中，断网、禁用脚本也能阅读。

当结构、流程或当前状态需要图文解释时，嵌入相应图示或截图，配上图注与文字说明。代码和大文件仍按文档中的 GitHub 入口及权限要求获取。

用户明确要求纯文本、仅 Markdown、其他格式或不落盘时，按指定方式交付。

[打开独立 HTML 项目交接示例](https://xiaofengshi.github.io/handoff-skill/examples/project-handoff.html) · [Markdown 审计源](examples/project-handoff.md)

## 使用方法

### 换个会话

```text
请使用 $session-handoff，把当前任务整理成可粘贴到新对话继续执行的交接提示词，保留决定、验证证据、授权范围和下一步。
```

### 交给别人

```text
请使用 $session-handoff，整理一份可以分享给协作者的交接文档。对方看不到我的本地文件和聊天记录。请使用 GitHub 固定版本，写清环境准备、运行与验证命令，明确尚未交付的必要依赖。
```

### Project

```text
请使用 $session-handoff，把整个项目交接给新维护者，通过 GitHub 分享。请覆盖目标、结构、依赖、整体能力与验证证据、运行维护、待办和第一项维护动作。使用对方可访问的固定版本，明确缺少的输入或权限。
```

[打开独立 HTML 项目交接示例](https://xiaofengshi.github.io/handoff-skill/examples/project-handoff.html)

[阅读一份完整、可执行的分享交接示例](examples/shared-handoff.md)

以下为结构示例；实际交接需要填写真实仓库和版本。

```text
目标
从 GitHub 上的固定版本继续导出功能。

获取资料
仓库 URL、完整 commit SHA、仓库相对路径。

准备环境
运行时、锁定依赖、输入数据与访问条件。

运行和验证
具体命令、预期结果，以及第一项可执行工作。

待满足条件
接收者需要配置自己的 API 凭据。
```

## 手动安装到 Codex

克隆本仓库后，运行仅依赖 Python 标准库的安装器。它遵循 CODEX_HOME，并拒绝覆盖已有安装。

```sh
git clone https://github.com/xiaofengShi/handoff-skill.git
cd handoff-skill
python3 scripts/install.py
```

Python ≥ 3.9. `python3 scripts/install.py --dest /path/to/skills/session-handoff` installs to a chosen skill directory. Existing directories and symlinks are never overwritten. Back up your old installation before updating. Remove only the installed skill directory to uninstall.

The package follows the SKILL.md format and includes Codex metadata. Other agents’ installation support depends on the host and the [Skills CLI](https://github.com/vercel-labs/skills). Core instructions are currently in Chinese; output follows the user's language. Recipients of a handoff do not need this skill installed. A handoff still requires the project's actual environment, permissions, inputs, and credentials.

## 构建与检查

主页和两份 README 由 site/content.json 生成，无需前端依赖或外部字体。

```sh
python3 scripts/build.py
python3 -m unittest discover -s tests
git diff --check
```

To regenerate the standalone HTML example, use Python 3.10+ with `python3 -m pip install -r requirements-examples.txt`, then run `python3 scripts/render_example.py` before the site build. Skill use, installation, and the site builder do not require this optional example-rendering dependency.

For local preview, run `python3 -m http.server 8000 --directory docs` and open `http://localhost:8000/`. To edit product copy, edit `site/content.json`; to change presentation, edit `site/index.html` or `site/assets/`, then rebuild. `examples/shared-handoff.md` documents an actual fixed-version checkout and website build.

## 贡献与许可

行为检查场景与贡献要求见 CONTRIBUTING.md。Skill 和安装器采用 MIT 许可。它提供供 Agent 遵循的工作流，不会自行运行任意项目。

[CONTRIBUTING.md](CONTRIBUTING.md) · [LICENSE](LICENSE)
