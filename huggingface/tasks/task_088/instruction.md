# Repair a boundary aggregation failure

A short time series fails when it is aggregated into a coarser bin. The same
workflow should run to completion and return a finite aggregate for valid
inputs.

Reproduce the issue from the supplied source snapshot and references, inspect
the implementation, and repair the behavior so the aggregation workflow works
for the supported coordinates. The fix must generalize beyond the public
example and must not hard-code a single span or output value.

Work only in this task directory. The evaluation environment is Linux and has
no network access. You may modify files under `source/`.

Use:

```bash
python reproduce.py
```

The command returns `1` for the reproduced scientific inconsistency, `0` after
a successful repair, and `2` for a runner or environment failure.
