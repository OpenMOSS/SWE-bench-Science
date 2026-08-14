# Repair an inconsistent GNSS point solution

A GNSS navigation workflow uses the supplied scientific package to solve for a
receiver state from satellite positions and corrected pseudoranges. The
calculation completes and returns finite coordinates, but the recovered
receiver state is materially offset from the supplied control state.

Run the public reproduction, inspect the complete source snapshot, and repair
the implementation so that the point-positioning workflow is scientifically
consistent. The repair must generalize to other valid measurement tables,
satellite constellations, epoch groupings, and receiver states. Do not
special-case the supplied fixture or replace the scientific calculation with
fixed output.

Work only in this task directory. The evaluation environment is Linux and has
no network access. You may modify files under `source/`.

Use:

```bash
python reproduce.py
```

The command returns `1` for the reproduced finite scientific inconsistency,
`0` after a successful repair, and `2` for a runner or environment failure.

