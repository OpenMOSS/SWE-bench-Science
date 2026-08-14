# Repair an inconsistent polymer coordinate workflow

A valid Polyply workflow using the supplied polymer fixture does not finish
cleanly on the provided source snapshot. The command can read the input files,
but the coordinate-generation run halts before it produces the expected output
coordinates.

Inspect the paper, the documentation, and the source snapshot; run the public
reproduction; and repair the implementation so the workflow completes on the
supplied fixture and remains correct for other valid inputs of the same
kind. Do not hard-code the supplied fixture or replace the scientific
workflow with a fixed output.

Work only in this task directory. The evaluation environment is offline. You
may modify files under `source/`.

Use:

```bash
python reproduce.py
```

The command returns `1` when the public workflow hits the reproduced scientific
failure, `0` after a successful repair, and `2` for a runner or environment
failure.
