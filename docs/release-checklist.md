# 设计审阅与发布检查表

## A. 设计冻结前

- [ ] 老师确认 HF repo id 和 private visibility
- [ ] 老师确认 Docker Hub namespace 与 verifier visibility
- [ ] 确认 119 个 release id，`001` 只含最终 payload 且无 legacy alias/history
- [ ] 确认 12 个 GPL-family task id
- [ ] 确认 HF 最小表格列和论文统计维度
- [ ] 确认 verifier tests 的披露策略
- [ ] 确认 Pier 最低版本和 task schema version
- [ ] 所有 upstream source license 已确认，无 `UNKNOWN` 占位

## B. 单题 002 canary

- [ ] environment image 可在 `linux/amd64` 拉取
- [ ] environment image 无 harness、私测和答案材料
- [ ] Pier 可按版本安装 Codex/Claude/mini-swe-agent 中至少一种
- [ ] 网关 base URL、wire protocol 和 key 只由 env/job config 提供
- [ ] collect hook 导出 binary-safe `model.patch`
- [ ] verifier image 为 separate environment，无网络
- [ ] verifier 在干净 baseline 应用 patch 并重新构建
- [ ] no-op 能失败，known-good 能通过
- [ ] 60/120 秒短测能产出 trajectory、artifact 和 reward

## C. 全量镜像

- [ ] 119 个 environment digests
- [ ] 119 个 verifier digests
- [ ] verifier 的 base digest 与对应 environment 完全匹配
- [ ] 所有常规镜像为 amd64；例外有书面记录
- [ ] 每题有 build log、SBOM、source/config fingerprint
- [ ] 镜像扫描无 secret、answer patch、agent harness 泄漏
- [ ] 不发布 `task-agent` 或 `119 x n` harness 镜像

## D. Hugging Face

- [ ] private dataset display title 为 `SWE-bench Science`
- [ ] Dataset Viewer 显示 119 行
- [ ] 统计表由 canonical rows 自动生成
- [ ] `default-107.json` 和 `all-119.json` 内容及 hash 正确
- [ ] task bundle 可下载到本地并由 Pier 读取
- [ ] image fields 使用最终 Docker Hub digest
- [ ] 无 solution/reference patch、密钥、旧运行输出
- [ ] dataset card 写明 license 与 GPL 入口

## E. 干净用户验收

- [ ] 从空目录下载 HF snapshot，不依赖旧 authoring GitHub
- [ ] 复制用户 `.env` 到本地 credentials 位置，不提交
- [ ] 拉取 002 environment/verifier images
- [ ] Pier 完成 120 秒短测
- [ ] 固定 selection 支持单题、任意列表、默认 107 和 opt-in 119
- [ ] 失败可按 task/trial 精确重试，不重新抽样
