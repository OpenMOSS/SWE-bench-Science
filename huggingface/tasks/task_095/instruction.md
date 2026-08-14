# Repair a repeated porous-electrode transport workflow

A porous-network workflow processes a compact sequence of electrode-like
stages. The inputs are finite and valid, and the calculation completes, but the
reported transport observations are not stable across the supplied control
stages.

Run the public reproduction, inspect the scientific notes and complete source
snapshot, and repair the implementation so the staged transport observations
are scientifically consistent. The repair must generalize to other valid pore
networks, stage orders, transport algorithms, and model parameters. Do not
special-case the supplied fixture or replace the scientific calculation with a
fixed report.

Work only under this task directory. The evaluation environment is Linux and
has no network access. You may modify files under `source/`.

Use:

```bash
python reproduce.py
```

The command returns `0` when the diagnostic workflow produces finite
observations and `2` for a runner or environment failure. The report is
diagnostic; the repair must be judged from the scientific behavior, not by
hard-coding one printed value.
