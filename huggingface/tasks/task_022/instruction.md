# Investigate a volume-to-surface projection anomaly

The supplied source is a real snapshot of a published neuroimaging analysis
library. In one volume-to-surface workflow, a volumetric product distributed
with an anatomical lookup table is mapped onto a cortical surface. The command
completes, but some finite surface values cannot be associated with any row of
that table.

Treat this as a scientific reproduction investigation rather than a textual
patch task. Inspect the source and the public reproduction,
reproduce the anomaly, and determine why the projected result is incompatible
with the accompanying scientific metadata. Repair the public
volume-to-surface workflow so that the result can be used in the downstream
analysis while other documented uses remain compatible.

The repair should generalize beyond the supplied example and should not be
specialized to one volume, surface, or lookup table. Preserve the library's
documented behavior for other supported inputs and geometries.

Do not hard-code the public volume, table entries, mesh, sample count, affine, or
expected output. Do not modify `reproduce.py`, the fixtures, or the evaluation
harness. Work inside the supplied source snapshot and keep the task runnable
without network access.

Run the public workflow with:

```bash
python reproduce.py
```

The initial snapshot is expected to report the observed scientific anomaly.
After your repair it should report `post_fix_success`. Generated files belong
under `outputs/`.
