# Complete 3-D Cross-n FOURIN Spectral Coupling

You are given a reduced source snapshot from a TERPSICHORE-style ideal MHD
stability workflow.

The current implementation handles simpler spectral settings, but the included
3-D plasma-only reproduction exposes an incomplete capability: cross-n spectral
coupling is not consistently preserved through the coefficient and downstream
matrix/energy path.

Inspect the source and run:

```bash
python reproduce.py
```

The reproduction writes the candidate workflow's raw observations under
`outputs/`. The command returns nonzero if those observations are empty,
incomplete, or non-finite; it does not apply verifier-only capability
thresholds.

Your task is to complete the implementation so that a genuinely
three-dimensional mode set with multiple toroidal `n` groups is handled
consistently.

The intended capability chain is:

```text
mode table -> trigonometric lookup -> branch metadata reduction -> FOURIN coefficients -> matrix assembly -> energy accounting
```

Do not hard-code:

- the included case;
- a fixed list of expected numbers;
- a fixed mode table;
- a single coefficient or matrix block.

Do not bypass the coefficient path by writing directly into matrix outputs. The
implementation should support the general 3-D spectral-coupling workflow
represented by the supplied task.

Internet access is not available during evaluation.
