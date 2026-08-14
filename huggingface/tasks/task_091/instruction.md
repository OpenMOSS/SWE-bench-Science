# Repair a workflow regression

A bundled input file exercises the public workflow and currently fails the
smoke test.

Run the public reproduction, inspect the complete source snapshot, and repair
the implementation so valid inputs are handled consistently across
representative cases. The repair must generalize to other valid input files and
similar inputs. Do not hard-code the bundled file or output.

Work only in this task directory. The evaluation environment is Linux and has
no network access. You may modify files under `source/`.

Use:

```bash
python reproduce.py
```

The command returns `1` for the reproduced finite inconsistency, `0` after a
successful repair, and `2` for a runner or environment failure.
