# Complete the Missing Response Capability

You are given a reduced source snapshot from a TERPSICHORE-style ideal MHD
stability workflow.

The current implementation already reproduces a simpler baseline regime.
However, the included public cases introduce richer response settings with
multiple coupled mode groups and radially localized transport behavior. In the
current source snapshot, the reproduced downstream behavior still looks too
close to the baseline regime across those settings.

Inspect the source and run:

```bash
python reproduce.py
```

The reproduction writes the observed baseline and target quantities under
`outputs/`. The command returns nonzero if those observations are empty,
incomplete, or non-finite; it does not apply verifier-only scientific
acceptance windows.

Your task is to complete the implementation so that these richer settings are
handled as genuinely supported scientific regimes.

The intended capability chain is:

```text
regime handling -> radial response profiles -> sideband/transport representation -> projection and pair support -> downstream blocks -> energy diagnostics
```

Do not hard-code:

- the included public case;
- a fixed list of expected numbers;
- a single mode table;
- one pair-support pattern;
- one coefficient tensor or one matrix block.

Do not bypass the scientific data path by writing directly into downstream
matrix or energy outputs. The implementation should support the general
workflow represented by the supplied task.

Internet access is not available during evaluation.
