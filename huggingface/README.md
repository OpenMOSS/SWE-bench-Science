---
pretty_name: SWE-bench Science
language:
  - en
tags:
  - code
  - software-engineering
  - scientific-computing
  - coding-agents
  - benchmark
  - long-horizon
  - harbor
  - pier
size_categories:
  - n<1K
license: mit
configs:
  - config_name: default
    data_files:
      - split: test
        path: data/tasks.csv
    features:
      - name: task_id
        dtype: string
      - name: science_knowledge_ablation
        dtype: bool
      - name: title
        dtype: string
      - name: domain
        dtype: string
      - name: language
        dtype: string
      - name: repository_url
        dtype: string
      - name: base_commit
        dtype: string
      - name: source_license
        dtype: string
      - name: gpl_family
        dtype: bool
      - name: restricted_license
        dtype: bool
      - name: license_gate
        dtype: string
      - name: material_license
        dtype: string
      - name: material_license_source
        dtype: string
      - name: material_restricted
        dtype: string
      - name: materials_gate
        dtype: string
      - name: materials_manifest_sha256
        dtype: string
      - name: material_licenses
        dtype: string
      - name: materials_provenance
        dtype: string
      - name: restricted_reason
        dtype: string
      - name: environment_image
        dtype: string
      - name: verifier_image
        dtype: string
      - name: image_platform
        dtype: string
      - name: task_path
        dtype: string
      - name: status
        dtype: string
---

# SWE-bench Science

SWE-bench Science evaluates coding agents on software-engineering tasks drawn from scientific-computing repositories. The release contains 119 tasks with isolated environments and separate programmatic verifiers.

- **GitHub release repository:** [OpenMOSS/SWE-bench-Science](https://github.com/OpenMOSS/SWE-bench-Science)
- **Runtime images:** [Docker Hub](https://hub.docker.com/u/kevinxulearning), pinned by immutable `linux/amd64` digests
- **Evaluation framework:** [Pier](https://github.com/datacurve-ai/pier), compatible with Harbor task format

## Dataset Summary

| Metric | Value |
| --- | ---: |
| Tasks | 119 |
| Default selection | 96 unrestricted-license tasks |
| Restricted selection | 23 tasks |
| GPL/LGPL/AGPL-family tasks | 18 |
| Environment images | 119 Docker Hub images |
| Verifier images | 119 Docker Hub images |
| Image platform | `linux/amd64` |

The `science_knowledge_ablation` column is `true` for the 91-task science-knowledge
split used by the ablation experiment. Its release IDs are `002-082`, `084`, `086`,
`090`, `097-101`, `111`, and `114`; all other rows are `false`.

## Dataset Viewer And Files

The Dataset Viewer reads the canonical [`data/tasks.csv`](data/tasks.csv) table and generates its preview automatically. The release does not commit a duplicate Parquet export, so the CSV remains the single source of truth for the 119 task rows.

The repository also includes:

| Path | Purpose |
| --- | --- |
| `data/tasks.csv` | Human-readable task table |
| `data/statistics.md` | Generated release statistics |
| `manifests/tasks.jsonl` | Canonical machine-readable release manifest |
| `selections/` | Reproducible task selections |
| `tasks/task_NNN/` | Thin Harbor/Pier task bundles |
| `tools/` | Materialization, provider, batch, and summary tools |
| `docs/run-batch.md` | Full provider and batch-runner reference |

The environment image contains the baseline source, public fixtures, dependencies, and compilers. The separate verifier image contains held-out tests and the grader. The dataset does not contain reference-answer patches, credentials, agent trajectories, or private verifier tests.

## Quick Start

~~~bash
python3 -m pip install "huggingface_hub[cli]"
hf auth login
hf download OpenMOSS-Team/SWE-bench-Science \
  --repo-type dataset --local-dir swe-bench-science
cd swe-bench-science

uv tool install "datacurve-pier==0.3.0"
docker login
~~~

Materialize the default selection:

~~~bash
python3 tools/materialize.py \
  --output tasks-selected --force
~~~

Materialize one task, a comma-separated list, or inclusive ranges:

~~~bash
python3 tools/materialize.py \
  --task-id 002,005-007 \
  --output tasks-selected-small --force
~~~

Materialize the complete 91-task science-knowledge ablation split. It contains
restricted-license tasks, so the explicit license opt-in is required:

~~~bash
python3 tools/materialize.py \
  --task-id 002-082,084,086,090,097-101,111,114 \
  --allow-restricted-licenses \
  --output tasks-science-knowledge-ablation --force
~~~

Every materialization writes `selection.json` with the exact task IDs used for the run.

## Restricted Licenses

Twenty-three tasks are excluded from the default selection because they contain GPL/LGPL/AGPL-family code, academic non-commercial sources or materials, or restricted third-party data. Include them only after confirming that your use is permitted:

~~~bash
python3 tools/materialize.py \
  --allow-restricted-licenses \
  --output tasks-selected-all --force
~~~

The GPL/LGPL/AGPL-family task IDs are `003, 020, 021, 023, 032, 057, 066, 074, 075, 082, 083, 084, 085, 096, 097, 098, 100, 118`. Tasks `019`, `026`, `035`, `043`, `101`, and `102` are restricted for other reasons. There is no `--allow-GPL` option. The selection flag controls which task bundles are materialized; it does not replace the upstream license obligations.

## Run An Evaluation

Run an infrastructure smoke with no model:

~~~bash
pier run -p tasks-selected-small \
  --agent nop --env docker \
  --n-concurrent 1 --n-attempts 1 \
  --no-force-build --no-delete --yes
~~~

Run a real agent by selecting a harness, model, and provider profile:

~~~bash
# Claude Code
pier run -p tasks-selected-small \
  --agent claude-code --env docker \
  --env-file ~/.config/swe-bench-science/claude.env \
  --model anthropic/claude-opus-4-7 --n-concurrent 1

# mini-swe-agent
pier run -p tasks-selected-small \
  --agent mini-swe-agent --env docker \
  --env-file ~/.config/swe-bench-science/mini-swe-agent.env \
  --model openai/gpt-5 --n-concurrent 1
~~~

For Codex gateway profiles, use the included wrapper:

~~~bash
python3 tools/run_batch.py \
  --path tasks-selected-small \
  --agent codex \
  --env-file ~/.config/swe-bench-science/codex.env \
  --n-concurrent 2 --n-attempts 1 \
  --jobs-dir jobs --job-name codex-small
~~~

For a short agent-stage smoke, add `--agent-timeout-multiplier 0.0223`, approximately 120 seconds for the default task timeout. Verifier and scientific-build timeouts remain independent.

## Provider Profiles

Create profiles outside the downloaded dataset:

~~~bash
mkdir -p ~/.config/swe-bench-science
cp profiles/codex.env.example ~/.config/swe-bench-science/codex.env
cp profiles/claude.env.example ~/.config/swe-bench-science/claude.env
cp profiles/mini-swe-agent.env.example ~/.config/swe-bench-science/mini-swe-agent.env
chmod 600 ~/.config/swe-bench-science/*.env
~~~

Codex profiles use `MODEL`, `OPENAI_API_KEY`, `CODEX_BASE_URL`, `CODEX_WIRE_API`, `CODEX_VERSION`, and `CODEX_REASONING_EFFORT`. Set `CODEX_WIRE_API=responses` for the OpenAI Responses API or `chat` for Chat Completions. Claude Code uses `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_BASE_URL`, and optional `ANTHROPIC_CUSTOM_HEADERS`. mini-swe-agent uses the provider variables expected by its selected model adapter.

Credentials are read at runtime. They are not stored in task metadata, Dockerfiles, image layers, or result summaries.

## Results

Pier writes one aggregate result and one trial directory per task and attempt:

~~~text
jobs/<job-name>/result.json
jobs/<job-name>/<task>__<trial>/verifier/reward.json
jobs/<job-name>/<task>__<trial>/verifier/ctrf.json
jobs/<job-name>/<task>__<trial>/verifier/test-stdout.txt
~~~

The wrapper additionally writes `jobs/summary.json` and `jobs/summary.csv`. For a direct Pier run, generate the same summaries with:

~~~bash
python3 tools/summarize_results.py --jobs-dir jobs
~~~

Use `pier view jobs` to inspect trajectories.

See [`docs/run-batch.md`](docs/run-batch.md) for the complete option reference,
gateway/profile configuration, dry-run mode, retry and timeout controls, and
result paths.

## Licensing And Attribution

The dataset card, release metadata, and helper tools use the repository's MIT terms. Task source, papers, figures, fixtures, and other third-party materials retain their upstream licenses. The source-license field does not automatically license copied scientific materials; audited material notices and modification notes are retained in the relevant task bundles.

The dataset is independent of GitHub at runtime. After download, materialization and evaluation use the local task bundle and the Docker Hub image digests recorded in `task.toml` and `data/tasks.csv`.
