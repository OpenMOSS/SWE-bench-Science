# Repair an inconsistent oriented-envelope fallback workflow

The supplied point-cloud workflow runs without an exception, but one of its
geometry-engine routes returns rectangles that are not consistent with the
documented minimum-area meaning of an oriented envelope. The same API is used
both for individual point clouds and for NumPy-compatible geometry batches.

Repair the supplied implementation so the public geometry API remains
offline, deterministic, and geometrically consistent for scalar and batch
workflows. Preserve the property aliases, degenerate point and line results,
and the shape, output-buffer, and container behavior expected by
NumPy-compatible array-like inputs.

Valid inputs may use coordinates with large but finite magnitudes, including
shapes far from the origin. A uniform scaling of an input must yield a
correspondingly scaled, finite result; intermediate arithmetic must not make a
valid finite computation fail.

Do not modify the fixtures or generated reports. Do not hard-code the public
sample or its derived geometry. Use the supplied source snapshot and public
reproduction to investigate the inconsistency.

Run the public diagnostic with:

```bash
python reproduce.py
```
