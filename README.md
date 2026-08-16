# SWE-bench Science

SWE-bench Science is a benchmark for evaluating coding agents on software-engineering tasks from scientific-computing repositories. The release contains 119 tasks spanning Python, C/C++, Fortran, MATLAB/Octave, and mixed-language projects.

The benchmark is distributed through two complementary repositories:

| Component | Contents |
| --- | --- |
| [Hugging Face dataset](https://huggingface.co/datasets/OpenMOSS-Team/SWE-bench-Science) | Task metadata, instructions, selections, thin Harbor/Pier bundles, and evaluation tools |
| [Docker Hub](https://hub.docker.com/u/kevinxulearning) | Immutable `linux/amd64` environment and verifier images |

The GitHub repository is the release and tooling repository. Evaluation uses the downloaded Hugging Face bundle and Docker Hub image digests; it does not fetch task definitions from GitHub at runtime.

## How A Task Is Evaluated

Each task uses two task-specific images:

- The **environment image** contains the baseline repository, public fixtures, dependencies, and compilers.
- The **verifier image** is separate and contains held-out tests and the grader.

Pier installs and runs the selected agent harness at evaluation time. Codex, Claude Code, mini-swe-agent, and other supported harnesses are evaluation choices; they are not duplicated into every task image.

The verifier collects the agent's committed changes as `model.patch`, applies them to a clean baseline, and runs the private tests. Native projects are rebuilt inside the task environment when required by the task.

## Requirements

- Python 3.11 or newer
- Docker Desktop or Docker Engine with `linux/amd64` support
- `uv` or another Python environment manager
- Access to the Hugging Face dataset and Docker Hub images
- Credentials for the selected model/provider when running a real agent

Apple Silicon hosts are supported through Docker Desktop's `linux/amd64` emulation.

## Quick Start

Download the release and install Pier:

~~~bash
git clone https://github.com/OpenMOSS/SWE-bench-Science.git
cd SWE-bench-Science

python3 -m pip install "huggingface_hub[cli]"
hf auth login
hf download OpenMOSS-Team/SWE-bench-Science \
  --repo-type dataset --local-dir .

uv tool install "datacurve-pier==0.3.0"
docker login
~~~

The Hugging Face dataset is the source for the task bundle. Docker Hub stores the runtime images referenced by the immutable digests in each `task.toml`.

## Select Tasks

The materializer writes an explicit `selection.json`, so a run is reproducible and does not depend on runner sampling behavior.

~~~bash
# Default selection: 96 unrestricted-license tasks.
python3 tools/materialize.py \
  --output tasks-selected --force

# One task, a comma-separated list, or inclusive ranges.
python3 tools/materialize.py \
  --task-id 002,005-007 \
  --output tasks-selected-small --force
~~~

Twenty-three tasks contain GPL/LGPL/AGPL-family code, academic non-commercial sources or materials, or restricted third-party data. They are excluded from the default selection and require an explicit opt-in:

~~~bash
python3 tools/materialize.py \
  --allow-restricted-licenses \
  --output tasks-selected-all --force
~~~

The GPL/LGPL/AGPL-family task IDs are `003, 020, 021, 023, 032, 057, 066, 074, 075, 082, 083, 084, 085, 096, 097, 098, 100, 118`. Tasks `019`, `026`, `035`, `043`, `101`, and `102` are restricted for other reasons. There is no `--allow-GPL` compatibility option.

## Run With Pier

Run an infrastructure smoke without a model:

~~~bash
pier run -p tasks-selected-small \
  --agent nop --env docker \
  --n-concurrent 1 --n-attempts 1 \
  --no-force-build --no-delete --yes
~~~

Run a real agent by selecting a harness and model/provider:

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

`--agent` selects the harness and `--model` selects the model/provider route. The credential file is read at runtime and is never copied into a task image or result artifact.

For a short agent-stage smoke, add `--agent-timeout-multiplier 0.0223`, which is approximately 120 seconds for the default task timeout. Verifier and scientific-build timeouts remain independent.

## Provider Profiles

Create provider profiles outside the checkout:

~~~bash
mkdir -p ~/.config/swe-bench-science
cp profiles/codex.env.example ~/.config/swe-bench-science/codex.env
cp profiles/claude.env.example ~/.config/swe-bench-science/claude.env
cp profiles/mini-swe-agent.env.example ~/.config/swe-bench-science/mini-swe-agent.env
chmod 600 ~/.config/swe-bench-science/*.env
~~~

Codex profiles use `MODEL`, `OPENAI_API_KEY`, `CODEX_BASE_URL`, `CODEX_WIRE_API`, `CODEX_VERSION`, and `CODEX_REASONING_EFFORT`. Set `CODEX_WIRE_API=responses` for the OpenAI Responses API or `chat` for Chat Completions. Claude Code uses `ANTHROPIC_AUTH_TOKEN`, `ANTHROPIC_BASE_URL`, and optional `ANTHROPIC_CUSTOM_HEADERS`. mini-swe-agent uses the provider variables expected by its model adapter.

For Codex gateway profiles, use the convenience runner so the profile is translated into the Codex `config_toml` format:

~~~bash
python3 tools/run_batch.py \
  --path tasks-selected-small \
  --agent codex \
  --env-file ~/.config/swe-bench-science/codex.env \
  --n-concurrent 2 --n-attempts 1 \
  --jobs-dir jobs --job-name codex-small
~~~

## Results

Pier writes one aggregate result and one trial directory per task and attempt:

~~~text
jobs/<job-name>/result.json
jobs/<job-name>/<task>__<trial>/verifier/reward.json
jobs/<job-name>/<task>__<trial>/verifier/ctrf.json
jobs/<job-name>/<task>__<trial>/verifier/test-stdout.txt
~~~

`tools/run_batch.py` additionally writes `jobs/summary.json` and `jobs/summary.csv`. For a direct Pier run, generate the same summaries with:

~~~bash
python3 tools/summarize_results.py --jobs-dir jobs
~~~

Use `pier view jobs` to inspect trajectories. When diagnosing a failure, inspect `result.json`, `reward.json`, and `test-stdout.txt` together.

## Data And Licensing

The Hugging Face dataset contains task metadata and thin task bundles. It does not contain reference-answer patches, credentials, agent trajectories, or private verifier tests. The canonical table is [`huggingface/data/tasks.csv`](huggingface/data/tasks.csv). Hugging Face Dataset Viewer reads this CSV and generates its preview automatically; no checked-in Parquet copy is required.

The project tools and documentation are released under the root MIT license. Task source, papers, figures, fixtures, and other third-party materials retain their upstream licenses. Audited material notices are included in the task bundles where applicable and summarized in [`NOTICE.md`](NOTICE.md).

## Documentation

- [Dataset contract](docs/dataset-contract.md)
- [Architecture](docs/architecture.md)
- [Release checklist](docs/release-checklist.md)
- [Hugging Face dataset card](huggingface/README.md)
