# Repair calibrated framework embedding relaxation

A framework-generation workflow uses the relaxed embedding mode to let slot
positions move during optimization while preserving the topology. On the
supplied lower-symmetry panel, the relaxed build currently completes but still
behaves inconsistently: some cases regress bond closure, some cases inflate the
cell, and a pinned control should remain unchanged.

Repair the implementation so the relaxed workflow behaves consistently on the
whole visible panel and generalizes beyond it. The public comparison checks
bond-closure drift, cell-volume blow-up, and a pinned no-op control.

Run the public reproduction, inspect the source and documentation, and repair
the implementation so the relaxed workflow behaves consistently on supported
inputs. The repair must generalize beyond the public panel and must not
hard-code the supplied topologies, building units, or numbers.

Work only in this task directory. The evaluation environment is offline. You
may modify files under `source/`.

Use:

```bash
python reproduce.py
```

The command returns `1` when the public comparison still shows an
inconsistency, `0` after a successful repair, and `2` for a runner or
environment failure.
