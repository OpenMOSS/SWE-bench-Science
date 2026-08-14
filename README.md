# SWE-bench Science Release

根目录 [MIT license](LICENSE) 只覆盖本项目自有的发布工具和文档。第三方题目材料
继续适用其 upstream license；请先阅读 [NOTICE.md](NOTICE.md) 和逐题元数据。

这是 **SWE-bench Science** 的独立发布整理仓库。它从旧 authoring 仓库读取公开
题目和私测，生成不带旧 Git 历史的发布 task bundle、Hugging Face 表格和按题目
分离的 environment/verifier 构建上下文。当前已导入 119 道题，002 有一个本地
`linux/amd64` canary 镜像对；其余镜像字段保持空白，等待 Docker Hub 命名空间和
逐题构建验收。

OpenMOSS GitHub 仓库只承担工具版本管理、构建审阅和发布控制面，不成为 HF 数据集
运行时下载源码的依赖。完整题目源码和私有测试仍只用于本地 staging 与 Docker
image 构建，不进入本仓库。

## 仓库边界

```text
旧 authoring 仓库（只读输入）
        |
        | 清洗、编号映射、许可审计
        v
本地 release 仓库（本仓库）
        |                         |
        | dataset rows/task 包   | image build manifests
        v                         v
Hugging Face dataset          Docker Hub
任务索引、统计、Pier 描述       environment/verifier images
```

核心结论：发布物是每题一个 task/environment image 和每题一个 verifier
image，共 `119 + 119` 个题目镜像。Codex、Claude、mini-swe-agent 等由 Pier
在评测时按 agent/version 选择和安装，不为每道题预发布一份 harness 镜像。

Pier 的 Docker backend 可能在评测机上临时派生
`environment + installed agent` 缓存镜像，因此跑完所有题和多个 agent 后，本地
缓存数量可能接近 `119 x n`。这些是运行时缓存，不是 Docker Hub 发布物，也不
进入 Hugging Face 每题表格。

## 当前内容

- [架构与发布契约](docs/architecture.md)
- [Hugging Face 数据与字段契约](docs/dataset-contract.md)
- [设计审阅与发布检查表](docs/release-checklist.md)
- [Hugging Face dataset card 草案](huggingface/README.md)
- `scripts/import_task.py`：从旧仓库导入单题，过滤答案/作者材料并生成 task
- `scripts/generate_huggingface.py`：生成 `huggingface/data/tasks.csv`、统计表、
  `default-107`/`all-119` 清单、119 个薄 task bundle 和随 dataset 下载的工具
- `scripts/materialize.py`：按明确题号清单展开本地 Pier task
- `scripts/run_batch.py`：按固定清单预拉取镜像并调用 Pier 批量评测
- `profiles/codex.env.example`：Codex 模型、网关、wire protocol 和版本示例
- `scripts/build_canary.py`：构建并检查一题本地 environment/verifier amd64 镜像
- `scripts/build_publish_batch.py`：按题号批量构建、推送 Docker Hub、记录 digest 并
  在每批完成后删除本批本地镜像和 build cache
- `scripts/validate_release.py`：编号、GPL、路径泄漏和镜像字段校验

## 当前阶段

当前阶段是 `batch-publish`：发布架构已冻结，119 个公开 task bundle 已导入，002
的 environment/verifier 已推送到 Docker Hub 并按 digest 运行过 no-op verifier。
正式发布仍需完成许可证复核、其余 Docker Hub digest、HF private dataset 上传和
干净用户验收。

## 开箱使用

在本地 release 仓库中运行：

工具需要 Python 3.9+；Python 3.11+ 自带 TOML 解析器，Python 3.10 及更早版本如
缺少 backport，先执行 `python3 -m pip install tomli`。

```bash
# 重新从旧 authoring 仓库导入一题（旧仓库不会被写入）
python3 scripts/import_task.py \
  --source-root /path/to/my_science_bench_platform_amd64 \
  --task-id 002 --force

# 生成 Viewer 表格与固定选择清单
python3 scripts/generate_huggingface.py

# 默认只展开 107 道非 GPL 题；需要 GPL 题时必须显式打开
python3 scripts/materialize.py --output /tmp/science-tasks --force
python3 scripts/materialize.py --allow-GPL --output /tmp/science-tasks-all --force

# 使用已发布的 Docker Hub digest；脚本会按 linux/amd64 预拉取两类镜像，
# 并把同一平台传给 Pier 派生的 agent image。默认 --no-delete，避免 Pier 删除预构建镜像。
python3 scripts/run_batch.py --path /tmp/science-tasks \
  --agent nop --n-concurrent 4 --n-attempts 1 \
  --env-file /path/to/openai.env

# 本地 canary 已经在 Docker daemon 中时跳过 registry pull
python3 scripts/run_batch.py --path tasks/task_002 \
  --agent nop --skip-pull --dry-run

# 校验发布边界；正式上传前加 --require-images
python3 scripts/validate_release.py

# 构建一题 linux/amd64 environment + verifier canary
python3 scripts/build_canary.py --task-id 002 --platform linux/amd64

# 发布默认 107 道非 GPL 题；每批 10 道，推送完成后清理本批本地镜像
HTTP_PROXY=http://host.docker.internal:7897 \
HTTPS_PROXY=http://host.docker.internal:7897 \
ALL_PROXY=http://host.docker.internal:7897 \
NO_PROXY=localhost,127.0.0.1,host.docker.internal \
python3 scripts/build_publish_batch.py --batch-size 10

# 从断点继续；已记录两个 Docker Hub digest 的题目会跳过
python3 scripts/build_publish_batch.py --batch-size 10 --resume

# 包含 12 道 GPL-family 题目时必须显式选择全量清单并打开开关
python3 scripts/build_publish_batch.py \
  --selection huggingface/selections/all-119.json \
  --allow-GPL --batch-size 10 --resume
```

使用 Python 3.11+ 的 Pier（DeepSWE 固定的 Harbor-compatible runner）运行已构建
的本地 task：

```bash
uv venv --python 3.12 .venv
uv pip install "git+https://github.com/datacurve-ai/pier.git"
DOCKER_DEFAULT_PLATFORM=linux/amd64 .venv/bin/pier run \
  --path tasks/task_002 --agent nop --env docker \
  --n-concurrent 1 --n-attempts 1 --no-force-build --no-delete --yes
```

正式 Codex/Claude 评测时，密钥和网关只通过 Pier 的 `--env-file`、agent env/kwarg
和 provider 配置传入；它们不写入 task.toml、CSV、Dockerfile 或镜像。模型生成的
`model.patch` 由 collect hook 导出到 trial artifact，verifier 在新容器中应用并
重新编译源码。`--allow-GPL` 只影响题号选择，不改变运行时评分逻辑。

对于 Codex，`run_batch.py` 会从所选 env profile 自动读取 `MODEL`、
`CODEX_BASE_URL`、`CODEX_WIRE_API=responses|chat`、`CODEX_VERSION` 和
`CODEX_REASONING_EFFORT`，生成 Pier 原生 `config_toml`，并默认使用一个仅修正
npm optional platform package 的运行时 Codex adapter。`OPENAI_API_KEY` 只由 Pier
加载到 agent 进程；切换中转站就是改用另一个 `--env-file`。其他 agent 仍可用重复
的 `--model`、`--agent-env` 和 `--agent-kwarg` 原样传给 Pier。
如果 `MODEL` 含有 provider 前缀（例如 `provider/model-name`），runner 会同时设置
Codex 的 `command_model_name`，避免 Pier 默认截断前缀导致网关路由失败；显式传入
同名 `--agent-kwarg` 时以用户值为准。
短测可以用 `--agent-timeout-multiplier 0.0223` 将本任务默认约 5400 秒 agent
上限压到约 120 秒；这只限制 agent 阶段，verifier 仍按自己的 timeout 运行。

## 明确禁止

- 不复制旧仓库 Git 历史或实验输出；
- 发布编号 `001` 只使用最终确认的 replacement payload；
- 不保留或公开任何 legacy id 的别名、目录或迁移历史；
- 不提交标准答案 patch、oracle solution、author notes 或密钥；
- 不把 agent harness 烘进每题发布镜像；
- 不把 GitHub URL 作为 Pier 读取任务定义的必要依赖。
