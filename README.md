# session-handoff

A context handoff skill for continuing work in a new conversation or sharing a GitHub-based handoff with another person.

将当前任务整理为下一位 Agent 或协作者能接手的上下文，保留目标、决定、实际状态、证据、授权范围和第一项可执行工作。支持中文自然语言触发，也可以显式调用 `$session-handoff`。

## 两种交接方式

| 方式 | 适用场景 | 交付要求 |
| --- | --- | --- |
| 同机续接 | 自己在同一机器换会话 | 可复制的续接提示词，包含必要的本地路径与现场状态 |
| 分享交接 | 转发给别人，或换一台机器继续 | 自包含文档、接收者可访问的 GitHub 仓库、固定 commit，以及获取、配置、运行和验证步骤 |

分享交接会识别尚未推送的改动、本地数据、私有服务、凭据和专用工具等依赖。依赖或权限未解决时，文档应明确阻塞项。它不会自动创建 GitHub 仓库、发布文件、授予权限或部署应用。

## 安装到 Codex

先通过实际发布仓库的 GitHub **Code** 按钮复制 clone 命令，或下载仓库 ZIP 并解压，进入包含本 README 的仓库根目录。发布前也可以直接使用已取得的仓库副本；本说明不预设尚未创建的远端地址。

在 macOS 或 Linux 的终端运行以下命令。安装步骤使用 Python 3 标准库，不需要额外 Python 包：

```sh
python3 - <<'PYINSTALL'
import os
import shutil
from pathlib import Path

source = Path('skills/session-handoff')
if not (source / 'SKILL.md').is_file():
    raise SystemExit('请先进入 session-handoff 仓库根目录。')
codex_dir = Path(os.environ.get('CODEX_HOME') or Path.home() / '.codex')
destination = codex_dir / 'skills' / 'session-handoff'
if destination.exists() or destination.is_symlink():
    raise SystemExit(f'目标已存在，请先检查并备份原安装：{destination}')
destination.parent.mkdir(parents=True, exist_ok=True)
shutil.copytree(source, destination)
print(f'Installed: {destination}')
PYINSTALL
```

安装后在下一轮对话中使用。若客户端未刷新技能列表，重新打开会话。

如果客户端原生扫描共享目录，也可以把整个 `skills/session-handoff/` 文件夹复制到 `~/.agents/skills/`；保留 `LICENSE`。其他客户端的发现机制和自动触发行为需按其文档确认，本项目没有验证所有客户端。无需同时安装到多个目录。

升级前先备份已有 `session-handoff`，再替换整个安装目录；安装命令会拒绝覆盖已有目录。卸载时移除你安装的这个目录即可，不涉及项目文件。

## 使用示例

### 自己换会话

```text
交接一下当前任务，整理成可以粘贴到新对话继续执行的提示词。
```

也可显式指定：

```text
请使用 $session-handoff，整理当前任务的状态、证据和接下来第一步。
```

### 分享给别人

```text
请使用 $session-handoff，把当前任务整理成可以分享给另一位协作者的交接文档。
对方看不到我的本地文件和聊天记录。代码与必要资料通过 GitHub 获取，
请写清固定版本、访问条件、从空目录开始的环境准备、运行命令和验证方式。
若有未交付的必要依赖，请明确说明。
```

分享文档应回答以下问题：

- 任务目标、当前状态和下一步是什么？
- 从哪个真实仓库、哪个完整 commit 获取代码？需要什么访问权限？
- 必要输入、配置和依赖从哪里获取？凭据如何由接收者自行配置？
- 如何安装、运行第一项任务，并判断结果正确？
- 哪些步骤已在独立目录验证，哪些仍未验证或受阻？

接收者无需安装本 Skill；交接文档本身应包含继续任务所需的说明和资料入口。使用者需具备项目实际要求的环境、权限和资源；一份文档不能自动提供私有仓库权限或运行凭据。

### 接手已有交接

```text
请接着下面这份交接继续工作，先核验当前规则、版本和易变状态，再执行已授权的下一步。
[在这里粘贴收到的交接内容]
```

请求“交接”只生成交接内容，不会自动创建新会话、写入持久记忆或启动下一阶段任务。分享文档中提到的历史授权也不能代替接收者当前用户的授权。

## 文件结构

```text
skills/session-handoff/
├── SKILL.md               # 交接流程与触发说明
├── LICENSE                # 安装包携带的 MIT 许可证
└── agents/openai.yaml     # Codex 展示信息与自动发现设置
```

Skill 是供模型遵循的工作流说明，不是自动运行项目的程序。它不附带特定项目的代码、数据或凭据。正文使用中文，描述字段包含英文；模型执行效果仍需按真实任务核验。

## 贡献与许可

贡献流程和需要检查的使用场景见 [CONTRIBUTING.md](CONTRIBUTING.md)。本项目采用 [MIT License](LICENSE)；分发安装目录时也需保留其中的许可证。
