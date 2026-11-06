# session-handoff

[English](README.md) · [Website](https://xiaofengShi.github.io/session-handoff/) · [Release](https://github.com/xiaofengShi/session-handoff/releases/tag/v0.1.0)

**保留上下文，让工作继续。**

把进行中的任务整理为能直接接手的上下文。保留关键决定、真实状态和下一步，交给新会话，或通过 GitHub 分享给另一位协作者。

![session-handoff preview](https://xiaofengShi.github.io/session-handoff//assets/social.png)

## 快速开始

```sh
npx skills add xiaofengShi/session-handoff --skill session-handoff
```

运行命令，选择使用的 Agent，然后提出交接请求。CLI 默认安装到当前项目；加上 -g 可全局安装。

需要 Node.js 22.20 或更新版本。不想依赖 Node？克隆仓库后使用 Python 安装器。

## 使用方法

### 换个会话

```text
请使用 $session-handoff，把当前任务整理成可粘贴到新对话继续执行的交接提示词，保留决定、验证证据、授权范围和下一步。
```

### 交给别人

```text
请使用 $session-handoff，整理一份可以分享给协作者的交接文档。对方看不到我的本地文件和聊天记录。请使用 GitHub 固定版本，写清环境准备、运行与验证命令，明确尚未交付的必要依赖。
```

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
git clone https://github.com/xiaofengShi/session-handoff.git
cd session-handoff
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

For local preview, run `python3 -m http.server 8000 --directory docs` and open `http://localhost:8000/`. To edit product copy, edit `site/content.json`; to change presentation, edit `site/index.html` or `site/assets/`, then rebuild. `examples/shared-handoff.md` documents an actual fixed-version checkout and website build.

## 贡献与许可

行为检查场景与贡献要求见 CONTRIBUTING.md。Skill 和安装器采用 MIT 许可。它提供供 Agent 遵循的工作流，不会自行运行任意项目。

[CONTRIBUTING.md](CONTRIBUTING.md) · [LICENSE](LICENSE)
