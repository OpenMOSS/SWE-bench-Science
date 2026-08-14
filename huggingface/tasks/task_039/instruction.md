# Repair a river-network sediment transport calculation

An Earth-surface modeling workflow uses the supplied source snapshot to
simulate bed-material pulses moving through a river network. The calculation
completes, but the resulting downstream history and stored river state do not
match the physical behavior described by the supplied material.

Run the public reproduction, study the complete Python source snapshot, and
repair the implementation so that the
transport calculation, stored material, and tracked sediment motion remain
scientifically consistent. The repair must generalize to other river networks,
hydraulic conditions, sediment records, and time steps. Do not
special-case the supplied fixture or replace the scientific calculation with a
fixed report.

Work only in this task directory. The evaluation environment is Linux and has no
network access. You may modify files under `source/`.

Use:

```bash
python reproduce.py
```

The command returns `1` for the reproduced finite scientific inconsistency, `0`
after a successful repair, and `2` for a runner or environment failure.
