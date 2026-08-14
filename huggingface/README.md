---
pretty_name: SWE-bench Science
language:
  - en
task_categories:
  - text-generation
tags:
  - software-engineering
  - code-agents
  - scientific-computing
  - benchmark
---

# SWE-bench Science

> Draft dataset card. Statistics and image references remain pending until the
> design contract is approved and the canonical 119-row dataset is generated.

SWE-bench Science evaluates coding agents on software-engineering problems from
scientific computing repositories. Each task is paired with an isolated task
environment and a separate verifier environment. Agent harnesses are selected
at evaluation time through Pier and are not baked into per-task release images.

## Dataset Summary

| Metric | Value |
| --- | ---: |
| Total tasks | 119 |
| Default non-GPL-family tasks | 107 |
| GPL/LGPL/AGPL-family opt-in tasks | 12 |
| Task environment images | pending |
| Separate verifier images | pending |
| linux/amd64 coverage | pending |

Domain, language, license, and verifier-status tables will be generated from
`data/tasks.parquet`; they will not be maintained manually.

## Task Format

Each row records a stable task id, title, scientific domain, implementation
language, upstream repository and base commit, source license, GPL-family gate,
task environment image, verifier image, and local Pier task path.

The downloadable task bundle follows the Harbor-compatible format consumed by
Pier. The task environment and verifier run in separate containers. A trial
exports the agent's Git diff as `model.patch`; the verifier applies it to a
fresh baseline, rebuilds the project, and runs the grading contract offline.

Pier currently runs local task directories rather than downloading this Hugging
Face dataset directly. The release therefore includes a small materialization
tool that resolves an explicit selection into a local `tasks-selected/`
directory before `pier run -p tasks-selected`.

## Agent Harnesses

Codex, Claude Code, mini-swe-agent, and other Pier-supported harnesses are trial
configuration. They are not dataset columns and are not published once per
task. Reproducible evaluation records pin the Pier version, agent/version,
model/provider configuration, installation fingerprint, and both image digests.

## GPL-family Tasks

The default download selection contains 107 tasks. Use the project download
tool's explicit `--allow-GPL` option to materialize all 119 tasks. This option
is a distribution selection and does not replace compliance with the upstream
license of each source repository.

## Security and Leakage Policy

The dataset does not distribute reference-answer patches, oracle solutions,
author notes, credentials, or previous agent trajectories. Verifier material is
never mounted into the agent environment. The verifier disclosure policy is
pending final confirmation by the dataset owners.

## Images

Image references will point to immutable Docker Hub digests after the owners
provide the final namespace and complete per-task validation. Blank image fields
mean unpublished, not "use a default image".

## Citation

Pending the final paper citation.

## License

Dataset metadata license: pending owner confirmation. Each task row records the
license of its upstream source repository separately.
