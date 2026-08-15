# Hugging Face 数据与字段契约

状态：`release-ready`

本契约面向 OpenMOSS 的 private Hugging Face dataset。Dataset Viewer 的表格是
老师要求的主要浏览入口；Pier task bundle 是下载后的运行入口。二者由相同的
release manifest 生成，不能人工维护两份不一致的数据。

## 1. 数据配置

建议只有一个 canonical split：

```text
huggingface/data/tasks.csv    119 rows, one row per release task
```

`default`（107 题）和 `with_gpl`（119 题）是下载 selection，不复制成两份数据
表。生成两个固定清单：

```text
selections/default-107.json
selections/all-119.json
```

运行工具默认读取前者；`--allow-GPL` 才允许读取后者。

由于 Pier 当前不能直接下载 HF registry dataset，HF snapshot 携带一个最小
materializer。用户先下载表格、selection 和 thin task bundle，再由它生成本地
`tasks-selected/`；其中 environment/verifier Dockerfile 只是 Pier 的格式入口，
源码和私测仍由已发布镜像提供。

## 2. Dataset Viewer 最小列

| 字段 | 类型 | 必填 | 说明 |
| --- | --- | --- | --- |
| `task_id` | string | 是 | 三位 release id，范围 `001..119` |
| `title` | string | 是 | 人类可读题目标题 |
| `domain` | string | 是 | 论文约定的科学领域 |
| `language` | string | 是 | 主要实现/构建语言 |
| `repository_url` | string | 是 | 上游源码仓库 |
| `base_commit` | string | 是 | 固定 40 位 commit SHA |
| `source_license` | string | 是 | SPDX 或经审阅的 family label |
| `gpl_family` | bool | 是 | 是否需要 `--allow-GPL` |
| `environment_image` | string | 是 | Docker Hub 引用，固定 digest |
| `verifier_image` | string | 是 | Docker Hub 引用，固定 digest |
| `task_path` | string | 是 | HF snapshot 中的本地 Pier task 目录 |

不把 `agent_name`、`agent_version` 或 `model` 放进 task row，因为这些是评测配置，
不是题目属性。它们进入独立的 evaluation results 表。

## 3. 内部 release manifest 字段

Dataset Viewer 不必展示但生成/审计必须保留：

```text
schema_version
release_version
task_id
source_tree_sha256
public_payload_sha256
environment_image_tag
environment_image_digest
verifier_image_tag
verifier_image_digest
image_platform
environment_build_fingerprint
verifier_build_fingerprint
source_license
license_source
gpl_family
agent_timeout_sec
verifier_timeout_sec
cpus
memory_mb
storage_mb
```

镜像 tag 便于人读，digest 才是运行锁。发布状态下两者都必须存在且能通过
registry manifest inspect 解析到 `linux/amd64`。

## 4. Evaluation results 表

agent/model 结果与 task table 分开：

| 字段 | 说明 |
| --- | --- |
| `run_id` | 全局运行标识 |
| `task_id` | release task id |
| `selection_sha256` | 固定题号清单 hash |
| `agent_name` / `agent_version` | Pier installed agent |
| `agent_install_fingerprint` | Pier 安装规格 hash |
| `model_name` | 模型标识 |
| `provider_protocol` | responses/chat/anthropic 等 |
| `pier_version` | runner 版本 |
| `environment_digest` / `verifier_digest` | 实际运行镜像 |
| `reward` | 主 reward |
| `public_passed` / `private_passed` | 子测试统计 |
| `failure_class` | candidate/infrastructure/timeout |
| `started_at` / `duration_sec` | 运行时间 |
| `trajectory_path` / `artifact_path` | 受控结果位置 |

## 5. Dataset card 统计

card 必须由 119 行 canonical data 生成以下表格，不能手填猜测数字：

- 总题数、默认题数、GPL-family 题数；
- scientific domain 分布；
- language 分布；
- source license 分布；
- environment/verifier image 完成度；
- amd64 覆盖率；
- verifier canary 通过/基础设施失败数。

已冻结的全局数字为：119 total、107 default、12 GPL-family。其余统计由发布脚本
从 canonical rows 自动生成；缺失值保留为空或 `UNKNOWN`，不会填零冒充统计结果。

## 6. 发布内容禁止项

HF snapshot、release Git 和两类 Docker image 都要扫描：

- `solution.patch`、`gold.patch`、`reference.patch`、answer commit；
- `solution/`、`oracle/`、`author_notes/`、provenance repair notes；
- `.env`、token、API key、认证 header；
- 旧运行 trajectories、model.patch、reward 和 workspaces；
- 非最终 `001` payload 和任何公开 legacy alias/history；
- agent harness binary/package（environment/verifier images 中）。

测试 patch 不等同于标准答案 patch，但是否随 HF 发布必须由 verifier disclosure
策略决定。无论是否公开，tests 不能进入 agent environment image。

## 7. 编号契约

- canonical task id 是字符串，不是整数，必须保留前导零；
- 只允许 `001` 到 `119`；
- 不提供 legacy redirect、alias 或兼容字段；
- 不从旧 Git history 导入提交；
- 一个 task id 必须唯一映射到一组 public payload、environment digest 和 verifier
  digest。

## 8. GPL selection

12 个 GPL-family release id：

```text
003 021 023 057 066 074 075 083 084 085 100 118
```

`default-107.json` 必须排除它们，`all-119.json` 必须恰好包含 119 个唯一 id。
`--allow-GPL` 只切换 selection；不修改任务内容，不绕过许可证 notice/source
义务，也不改变 Pier 行为。
