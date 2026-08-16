# Release Verification

This checklist records the published SWE-bench Science release and its
operational verification steps.

## Release Artifacts

- [x] 119 canonical release ids (`001` through `119`), with the replacement
      payload used for `001` and no legacy id exposed.
- [x] 18 GPL-family ids, one academic non-commercial source id, one id with
      academic non-commercial auxiliary material, and two restricted-material
      ids are separated from the default selection.
- [x] 119 environment image digests and 119 verifier image digests are recorded.
- [x] Every published image resolves to `linux/amd64`.
- [x] Every verifier image is based on the corresponding environment digest.
- [x] GitHub release repository is `OpenMOSS/SWE-bench-Science`.
- [x] Hugging Face dataset is `OpenMOSS-Team/SWE-bench-Science`.
- [x] Docker Hub namespace is `kevinxulearning`; GHCR is not used.

## Dataset Integrity

- [x] Dataset Viewer table is generated from the canonical 119-row manifest.
- [x] `default-97.json` excludes exactly the 22 restricted-license ids.
- [x] `all-119.json` contains exactly 119 unique ids.
- [x] Task bundles contain no reference-answer patch, credential, trajectory, or
      private verifier test.
- [x] Environment and verifier digests are immutable Docker Hub references.
- [x] README and dataset card describe the actual repository ids and commands.

## Runtime Verification

- [x] A clean clone can materialize task 002 without the authoring repository.
- [x] Docker Hub environment and verifier images can be pulled as `linux/amd64`.
- [x] Pier can install the selected Codex runtime and connect through the
      configured gateway profile.
- [x] The separate verifier runs in a fresh no-network container and writes
      `reward.json`, `ctrf.json`, `test-stdout.txt`, and `run.log`.
- [x] The batch wrapper writes `jobs/summary.json` and `jobs/summary.csv` after
      Pier exits.

The 002 short smoke intentionally uses an unsolved baseline, so its agent trial
may receive `AgentTimeoutError` and reward `0.0`. That outcome is a candidate
result, not an infrastructure error; the public/private verifier output remains
available for diagnosis.

## User-Facing Interfaces

- [x] Exact task ids, comma-separated ids, and inclusive ranges are supported.
- [x] The default unrestricted selection and full
      `--allow-restricted-licenses` selection are reproducible through
      `selection.json`.
- [x] Direct Pier commands and the optional `run_batch.py` wrapper are documented.
- [x] Codex Responses/Chat, Claude Code, and mini-swe-agent profile examples are
      included without credentials.
- [x] Results can be inspected with `pier view` or the generated JSON/CSV summary.
