# Shared handoff: build the session-handoff website

This is a real, minimal example of a handoff to someone who cannot access the sender’s machine or chat history. The task is to build this project’s static website from a fixed public revision. It is not an example of handing off a production deployment.

## Goal and current state

Build and preview the bilingual session-handoff homepage. The source, static assets, installer, and installation tests are included in the repository at the revision below. Product copy lives in `site/content.json`; `scripts/build.py` generates `docs/`, `README.md`, and `README.zh-CN.md`.

- Repository: https://github.com/xiaofengShi/handoff-skill
- Fixed commit: `df15d0a35df79a1f52f501b1eb9a50d2ca0db798`
- Read first: [README.md](https://github.com/xiaofengShi/handoff-skill/blob/df15d0a35df79a1f52f501b1eb9a50d2ca0db798/README.md), [CONTRIBUTING.md](https://github.com/xiaofengShi/handoff-skill/blob/df15d0a35df79a1f52f501b1eb9a50d2ca0db798/CONTRIBUTING.md), then [scripts/build.py](https://github.com/xiaofengShi/handoff-skill/blob/df15d0a35df79a1f52f501b1eb9a50d2ca0db798/scripts/build.py).
- Access: public repository; no GitHub login is needed to clone over HTTPS.
- Requirements: Git and Python 3.9 or newer. A shell is needed for the commands below; they use macOS/Linux shell syntax. No Node.js, Python packages, credentials, private data, or original chat history are needed for this build task.

## Run from an empty directory

Run in a directory that does not already contain `session-handoff-example`:

```sh
git clone https://github.com/xiaofengShi/handoff-skill.git session-handoff-example
cd session-handoff-example
git checkout --detach df15d0a35df79a1f52f501b1eb9a50d2ca0db798
python3 scripts/build.py
python3 -m unittest discover -s tests
git diff --exit-code
python3 -m http.server 8000 --bind 127.0.0.1 --directory docs
```

Expected results:

1. The build prints `Built docs/, README.md, and README.zh-CN.md`.
2. Both installation tests pass and the test runner prints `OK`.
3. `git diff --exit-code` returns zero: rebuilding produces the committed views without changes.
4. Open `http://127.0.0.1:8000/` for English or `http://127.0.0.1:8000/zh/` for Chinese. The website should render without remote fonts or frontend packages. Stop your own preview server with Ctrl+C when finished.

If port 8000 is occupied, choose another free port and use that port in the local URL. Do not stop another person’s process.

## Next action and success condition

The first action is the fixed-version build and test sequence above. Success means it passes from this public checkout and both local pages can be opened. No pending private dependency is needed for this task. This example does not require installing the skill itself, publishing changes, or modifying repository settings.

Any later task or external write must follow the recipient’s current user instructions and environment permissions. The sender’s historical authorization does not grant access to the recipient.

## 中文说明

这是一份真实的分享交接示例：接收者只需 Git、Python 3.9+ 和公开仓库，就能按上面的固定 commit 构建、测试并预览中英主页，无需发送者本地文件、聊天记录、密钥或私有数据。请按顺序运行命令，确认构建成功、两项测试通过且重新构建没有产生 diff，再打开本地地址。此任务仅验证本地构建，不授权推送、部署或修改远端设置。
