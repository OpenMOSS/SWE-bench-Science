# SWE-bench Science 架构与发布契约

状态：`canary`

本文档冻结职责、发布边界和验收条件。当前 119 个 task bundle 已导入，task 002
的 environment/verifier amd64 canary 已完成隔离和 Pier 端到端验收。

## 1. 目标

SWE-bench Science 的发布需要同时满足：

1. 119 道题可以作为 Hugging Face dataset 查看、筛选和下载；
2. 每道题有可复现、优先为 `linux/amd64` 的 task/environment image；
3. 每道题有与 agent 隔离的 verifier image；
4. Codex、Claude Code、mini-swe-agent 等 harness 可以在运行时选择，而不导致
   Docker Hub 发布 `119 x n` 份题目镜像；
5. verifier 能在干净源码上应用 agent patch，并重新编译 C/C++ 等任务；
6. 发布物不包含标准答案 patch；
7. 107 道默认题和 12 道 GPL-family 题有明确但非强制的下载入口；
8. Hugging Face + Docker Hub 可以独立于 GitHub 工作。

## 2. 官方 benchmark 核对结论

### 2.1 DeepSWE

DeepSWE 的每道题包含 `task.toml`、`instruction.md`、`environment/`、`tests/`
和 `solution/`。截至核对时，其 113 道题各有一个 environment Dockerfile 和一个
tests/verifier Dockerfile。`task.toml` 把 agent 环境设为预构建镜像，并把
verifier 设为 `environment_mode = "separate"`。

DeepSWE 的 tests Dockerfile 直接 `FROM` 对应的 task environment image，再复制
held-out tests 和 grader。这证明 task environment 与 verifier 是两个按题目的
容器角色。[DeepSWE task format](https://github.com/datacurve-ai/deep-swe#task-format)
和[示例 task.toml](https://github.com/datacurve-ai/deep-swe/blob/main/tasks/abs-module-cache-flags/task.toml)
是本设计的主要参考。

DeepSWE 的公开 GitHub authoring 仓库包含 `solution.patch`，但其 README 明确说明
该 patch 不参与评分。老师对本数据集提出了更严格的发布要求，因此 SWE-bench
Science 的 HF/release 仓库**不复制这一部分**：标准答案只可留在独立、受控的
作者材料区，不能进入本仓库、HF dataset 或镜像。

### 2.2 Pier

Pier 是 Harbor-compatible runner。它支持 `codex`、`claude-code`、
`mini-swe-agent`、`gemini-cli`、`opencode` 等 installed agents，并为无公网题目
提供 agent 安装和推理域名的网络 allowlist。
[Pier README](https://github.com/datacurve-ai/pier#why-pier)

Pier 的 Docker 实现不是从一个完全独立的 harness 容器挂载题目环境。它会：

1. 读取 task 的预构建 `environment.docker_image`；
2. 根据 agent/version 生成安装规格和 fingerprint；
3. 创建临时 Dockerfile：`FROM <task environment image>`；
4. 追加 Codex/Claude/mini-swe-agent 安装步骤；
5. 构建并缓存本次评测使用的派生镜像。

对应实现可见
[agent_setup.py](https://github.com/datacurve-ai/pier/blob/main/src/pier/environments/agent_setup.py)
和
[Docker environment](https://github.com/datacurve-ai/pier/blob/main/src/pier/environments/docker/docker.py)。

因此要区分两种数量：

| 范围 | 数量 | 是否发布 |
| --- | ---: | --- |
| task/environment images | 119 | 是 |
| verifier images | 119 | 是 |
| Pier 在评测机派生的 environment + agent 缓存 | 最多接近 `119 x n` | 否 |
| 单独的每题 harness 发布镜像 | 0 | 否 |

Pier 的派生缓存是让 agent CLI 和题目编译/运行依赖处于同一个 sandbox 的实现
细节。它不应成为 HF 表格里的 `task_agent_image`，也不应提前推送到 Docker Hub。

### 2.3 SWE-bench 与 Terminal-Bench

SWE-bench 将镜像分为 base、environment 和 instance 层，agent 生成 patch 后由
evaluation harness 在 instance container 中应用 patch 并执行测试。agent
harness 本身不是每题发布镜像。
[SWE-bench Docker setup](https://github.com/swe-bench/SWE-bench/blob/main/docs/guides/docker_setup.md)

Terminal-Bench 明确区分“task dataset”和“execution harness”；Harbor task
format 使用 task environment 与 verifier 配置，agent 由运行命令选择。
[Terminal-Bench README](https://github.com/harbor-framework/terminal-bench-1)

这些项目的共同点是**职责分离**，而不是必须存在三套公开 Docker 镜像。

## 3. 目标运行模型

```text
Hugging Face task row / local task.toml
                  |
                  v
        +---------------------+
        | E_i: environment    |
        | source + deps/tools |
        +----------+----------+
                   |
        Pier installs selected harness
        (agent/version fingerprint)
                   |
                   v
        +---------------------+
        | ephemeral E_i + A_j |
        | agent works in /app/task_NNN |
        +----------+----------+
                   |
          collect model.patch
                   |
                   v
        +---------------------+
        | V_i: verifier       |
        | FROM exact E_i      |
        | private tests/grader|
        +---------------------+
```

其中：

- `E_i` 是第 i 题发布到 Docker Hub 的 environment image；
- `A_j` 是 Pier 内置的 agent 安装规格，不是第 i 题的发布镜像；
- `V_i` 是第 i 题发布到 Docker Hub 的 verifier image；
- `model.patch` 是一次 trial 的输出，不是 dataset 内容；
- verifier 使用新的容器和干净工作树，不能沿用 agent 产生的二进制或测试状态。

## 4. task/environment image 契约

每道题恰好有一个 release environment image。它应包含：

- 题目源码的固定 baseline commit；
- 题目运行需要的公开 fixture 和公开 reproduction；
- 完成题目所需语言运行时、编译器、系统库和离线依赖；
- Git、shell 和 Pier installed agent 所需的基础工具；
- 工作目录 `/app/task_NNN`，且 baseline 位于可提交的正常分支；
- 无 future branch/tag/reflog 可泄露参考修复。

它不得包含：

- 标准答案 patch、answer commit、oracle solution；
- private verifier tests、grader 或 verifier 配置；
- Codex、Claude、Kimi、mini-swe-agent 等 harness；
- API key、网关地址的私有凭据或用户 `.env`；
- 旧实验 trajectory、reward、输出目录；
- legacy task id、旧 payload 或迁移历史信息。

`instruction.md` 由 HF task bundle 交给 Pier，不要求复制进 environment image。
这样 prompt 可以审阅和版本化，又不会把 task definition 与镜像文件系统重复绑定。

镜像默认/优先构建为 `linux/amd64`。如某题只能在其他平台运行，必须作为经审阅
的逐题例外写入 manifest，不能静默产生多架构不一致。

## 5. agent harness/runtime 契约

agent 是 trial 配置，不是 task row 的固有属性。运行时至少记录：

```text
agent_name
agent_version
model_name
provider_protocol
base_url (可公开规范化值，不含 secret/query)
reasoning_effort
Pier version
agent install fingerprint
```

连接中转站和密钥由 Pier job/CLI 配置提供：

- `agent.env` 传入 `OPENAI_API_KEY`、`ANTHROPIC_AUTH_TOKEN` 等；
- Codex 的 `kwargs.config_toml` 指定 model provider、`base_url`、`wire_api` 和
  `env_key`；
- `model_name` 只负责模型/结果元数据，不能隐式决定密钥；
- Pier 根据配置中的 URL 生成 agent 网络 allowlist；
- `.env` 文件只在运行机存在，不进入 task.toml、HF、镜像或 trial 公开日志。

首选 Pier installed-agent 路径，因为它与 DeepSWE 机制一致，并已支持 Codex、
Claude Code、mini-swe-agent。自定义 runner 只作为 Pier 无法表达某个已确认需求时
的后备方案，不能与 Pier 并行维护两套主流程。

## 6. verifier image 契约

每道题恰好有一个 verifier image，推荐：

```dockerfile
FROM <exact-environment-image-by-digest>
COPY test.sh grader.py config.json /tests/
COPY private_tests/ /tests/private_tests/
```

要求：

- `FROM` 必须对应同一题 environment image 的不可变 digest；
- verifier 运行时无 task 网络；
- 只接收 collect hook 导出的 `model.patch` 和允许的 trial 元数据；
- 在新的 baseline worktree 应用 patch；
- 删除/忽略 agent build outputs；
- 重新执行 build，再执行 public/private tests；
- 输出 `reward.json`、`ctrf.json`、`test-stdout.txt` 和 `run.log`；
- 区分 candidate failure 与 infrastructure failure；
- 不执行或读取标准答案 patch。

`[verifier.environment].docker_image` 可以直接记录预构建 verifier 镜像；同时可在
私有 authoring 输入中保留 tests Dockerfile 以支持可复现重建。HF 是否公开 tests
由老师决定，但 agent 隔离和“不含标准答案”是无条件要求。

## 7. 编译型题目

C/C++、Fortran、Rust、Octave 及带原生扩展的 Python 题必须区分三个阶段：

1. **镜像构建**：安装编译器、headers、CMake/Make 等依赖；可以编译 baseline
   以验证环境，但该产物不是评分输入。
2. **agent trial**：agent 可以在 `/app` 内反复编译和运行公开 reproduction。
3. **verifier trial**：新容器中应用 source patch，清理 build/dist/native objects，
   从源码重新编译，再运行评分测试。

patch 造成的合法编译失败计为题目失败；镜像缺少编译器、依赖或入口点计为基础
设施失败。二者必须在结果表中分开。

## 8. Harbor/Pier task bundle

HF 中每道题的最小可运行描述建议为：

```text
tasks/task_001/
├── task.toml
└── instruction.md
```

当 verifier 已预构建且入口点在 verifier image 中时，HF bundle 只携带
`task.toml`、`instruction.md` 和供 Pier 校验格式的薄 `environment/Dockerfile` /
`tests/Dockerfile` 入口。完整 source/build context 只保留在本地 release 工作区，
通过 `--include-build-context` 显式展开；标准答案目录永不导出。

建议的 `task.toml` 结构：

```toml
schema_version = "1.3"
artifacts = ["/logs/artifacts/model.patch"]

[task]
name = "openmoss/task-001"

[metadata]
task_id = "001"
language = "python"
base_commit_hash = "<sha>"

[agent]
network_mode = "no-network"
timeout_sec = 5400.0

[environment]
docker_image = "<dockerhub-environment-image>@sha256:<digest>"
os = "linux"
allow_internet = false
cpus = 2
memory_mb = 8192
storage_mb = 20480

[verifier]
network_mode = "no-network"
environment_mode = "separate"
timeout_sec = 1800.0

[verifier.environment]
docker_image = "<dockerhub-verifier-image>@sha256:<digest>"
os = "linux"
allow_internet = false
cpus = 2
memory_mb = 8192
storage_mb = 20480

[[verifier.collect]]
command = "cd /app && mkdir -p /logs/artifacts && git add -A && git diff --cached --binary <base> > /logs/artifacts/model.patch"
timeout_sec = 300.0
```

Docker Hub 是当前约定，不作为 runtime hostname 校验条件。表格中的镜像字段在
老师提供最终链接前保持空值，不能填入猜测的 namespace。

## 9. HF、Docker Hub 与 GitHub 的关系

### Hugging Face

OpenMOSS 下的 private dataset 是发布索引和可下载任务包，display title 为
`SWE-bench Science`。最终 repo id 由组织权限和命名规范确认，本文暂写作
`openmoss/SWE-bench-Science`，不提前创建远端。

HF 包含：数据表、统计、dataset card、task.toml、instruction，以及经批准的
可公开任务材料。HF 不包含标准答案 patch、密钥和本地运行输出。

### Docker Hub

Docker Hub 保存二进制运行环境：119 个 environment images 和 119 个 verifier
images。HF 每行用 digest 引用它们。镜像 namespace 和可见性由老师后续提供；
本设计不兼容/发布 GHCR，但也不在运行时硬编码 registry hostname 检查。

### GitHub

GitHub 不是 HF + Docker Hub 的运行依赖。若以后创建 OpenMOSS GitHub 仓库，
它只用于：

- 发布工具版本控制；
- CI 和构建 manifest 审阅；
- 文档和 issue；
- 生成 HF snapshot。

Pier 运行时读取的是从 HF 下载到本地的 task bundle，不需要再访问 GitHub 获取
题目定义。上游源码已经固化在 environment image 中。

Pier 当前不直接解析或下载 HF registry dataset，因此需要一个显式 materialize
步骤：先用 Hugging Face API 下载 card、canonical rows、selection 和 task files，
再在本地生成一个只含所选题目的 `tasks-selected/` 目录，最后执行
`pier run -p tasks-selected`。此过程完全不需要 GitHub。

## 10. 编号和历史

最终 release 只有 `001` 到 `119` 共 119 个编号：

- `001` 只对应最终确认的 replacement payload；
- 不在 HF、Docker tag、task.toml、README 或公开 manifest 中保留 legacy id；
- 旧编号转换只允许存在于一次性、本地且不提交的导入配置中；
- 新仓库从空 Git 历史开始，不复制旧仓库 commits。

## 11. GPL-family 入口

GPL-family 不是 DeepSWE/Pier 字段，而是本项目的分发选择策略：

- 默认下载/构建清单包含 107 道非 GPL-family 题；
- `--allow-GPL` 明确选择全部 119 道；
- 12 道 gated release id 为 `003, 021, 023, 057, 066, 074, 075, 083,
  084, 085, 100, 118`；
- Pier 本身只运行已经下载到本地的目录，不负责解释 GPL flag；
- 该入口不替代上游 license、notice、source offer 等实际合规义务；
- 按此前约定，不做 Docker registry hostname 的强制检查。

`--allow-GPL` 的具体入口属于 HF materializer：默认只 materialize/pull
`default-107.json` 中的任务和镜像，显式传入该参数后才读取 `all-119.json`。
直接对已经 materialize 的目录运行 Pier 不再重复做 license gate。

## 12. 批量评测

固定抽样必须先生成并保存明确题号清单，再交给 Pier，不能依赖不同版本 runner
可能不支持或语义变化的 `--sample-seed`：

```text
HF rows -> license filter -> explicit task-id selection.json
       -> materialize local tasks/<id>
       -> pier run -p <materialized directory>
       -> one trial per task/agent/model/replicate
       -> aggregate reward + failure class + image digests
```

批量运行记录至少包含：selection file hash、task ids、agent/version、model、provider
protocol、Pier version、environment/verifier digests、timeout、seed（若采样）、
replicate id 和结果路径。失败重试只重跑明确 task/trial，不重新抽样。

## 13. 发布阶段

1. **设计冻结**：审阅本文和字段契约，不构建/上传。
2. **单题 canary**：只导入 `002`，构建 amd64 environment + verifier，执行 no-op、
   oracle/known-good、60/120 秒 agent smoke。
3. **HF canary**：上传一行 private dataset，验证 Dataset Viewer、任务下载和 Pier
   本地运行；确认无 solution patch。
4. **批量构建**：由老师确认 Docker Hub namespace 后生成 119 + 119 镜像；每题
   记录 digest、SBOM、build log 和 verifier smoke。
5. **全量 HF**：生成 119 行、统计表、GPL 两个 selection manifest 和 task bundle。
6. **新用户验收**：从全新目录下载 HF、配置 `.env`、运行 002，再跑固定批量清单。

任何阶段失败都不得用空 digest、伪造统计或旧 GHCR 链接继续发布。

在全量发布前，所有 `source_license = UNKNOWN` 必须通过上游 LICENSE/COPYING、
仓库声明或人工审阅解析。无法确认许可证的任务不能靠默认值进入发布集。

## 14. 待老师确认的决策

以下项目在实现前仍需确认，但不阻塞本地设计仓库建立：

- Docker Hub organization/namespace 和 image visibility；
- verifier image 是否允许成员拉取并离线查看测试；
- HF repo id 的最终大小写/连字符形式；
- HF task bundle 是否附带 environment/tests Dockerfile，或只放预构建 digest；
- dataset card 的论文链接、作者、citation 和许可证；
- 结果表是否需要公开 agent trial trajectory。

## 15. 本地 release 仓库的目标布局

设计通过后，本仓库按下面的单向生成关系扩展：

```text
swe-bench-science-release/
├── docs/                         # 架构、字段、审阅记录
├── manifests/
│   └── tasks.jsonl               # 119 题 canonical release manifest
├── profiles/
│   └── codex.env.example         # Pier provider 模板，不含真实密钥
├── templates/
│   ├── environment/              # environment Dockerfile 模板
│   ├── task-tests/               # 预构建 verifier 的薄入口
│   └── verifier/                 # verifier Dockerfile/entrypoint 模板
├── huggingface/                  # HF card、data、selection、薄 task bundle
│   ├── tools/                    # 随 HF 下载的 materializer/batch runner
│   └── profiles/                 # 不含密钥的 provider 示例
├── scripts/                      # 导入、生成、校验、构建和 Pier 批量入口
└── tests/                        # release tooling tests
```

以下目录只存在于本机并由 `.gitignore` 排除：

```text
imports/       旧 authoring 仓库的只读导入快照
private/       经授权的 verifier/作者材料
build/         Docker build contexts 和 logs
staging/       尚未通过扫描的中间产物
dist/          待上传的 HF snapshot/release bundle
secrets/       Docker Hub/HF/provider credentials
jobs,trials/   Pier 运行结果
tasks/         逐题完整源码/build context；由 importer 本地生成，不进入 Git
```

数据流只能是 `imports/private -> validate -> staging -> dist`。不能从 `dist` 反向
修改 canonical manifest，也不能把整个旧仓库复制进新 Git。每个生成步骤最终都
要由 manifest hash 和可重放命令描述。
