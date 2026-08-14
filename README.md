# SWE-bench Science Release

这是 **SWE-bench Science** 的独立发布整理仓库。目前只包含已经核对过的
发布架构、Hugging Face 数据字段契约和审阅清单，不包含 runner、构建脚本、
题目源码、私测或标准答案。

本仓库不绑定 GitHub remote。后续即使不创建 GitHub 仓库，也可以作为本地
发布工作区生成 Hugging Face dataset 和 Docker Hub 镜像清单；如将来在
OpenMOSS 下建立 GitHub 仓库，它只承担工具版本管理和审阅，不成为 HF 数据集
运行时依赖。

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

## 当前阶段

当前阶段是 `design-review`。在架构文档通过审阅前，不实现构建、上传、下载或
评测代码，也不向 GitHub、Hugging Face 或 Docker Hub 写入任何内容。

## 明确禁止

- 不复制旧仓库 Git 历史或实验输出；
- 发布编号 `001` 只使用最终确认的 replacement payload；
- 不保留或公开任何 legacy id 的别名、目录或迁移历史；
- 不提交标准答案 patch、oracle solution、author notes 或密钥；
- 不把 agent harness 烘进每题发布镜像；
- 不把 GitHub URL 作为 Pier 读取任务定义的必要依赖。
