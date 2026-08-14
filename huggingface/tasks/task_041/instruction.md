# Repair an inconsistent near-Earth vector conversion

A space-physics instrument workflow uses the supplied scientific package to
convert a catalogue of Cartesian direction vectors between near-Earth
coordinate systems. The calculation completes and returns finite coordinates,
but the converted catalogue does not satisfy the scientific geometry described
by the supplied material.

Run the public reproduction, study the complete source snapshot, and repair the
implementation so that the
coordinate workflow is scientifically consistent. The repair must generalize
to other valid vector catalogues, coordinate systems, observation times, and
frame attributes. Do not special-case the supplied fixture or replace the
scientific calculation with fixed output.

Work only in this task directory. The evaluation environment is Linux and has
no network access. You may modify files under `source/`.

Use:

```bash
python reproduce.py
```

The command returns `1` for the reproduced finite scientific inconsistency,
`0` after a successful repair, and `2` for a runner or environment failure.
