Run `python reproduce.py` from this task directory and inspect the bundled
source snapshot and offline workbench.

The current preflight is small on purpose, but it exercises a boundary case
that should not be treated as valid. Repair the package code in `source/` so
the workbench reaches the expected post-fix status without changing the
fixture, the public runner, or the task metadata.

Keep the repair general. The corrected code should remain sensible for other
valid materials inputs, not only for the supplied local case.
