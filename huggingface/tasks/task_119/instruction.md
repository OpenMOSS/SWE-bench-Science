# Repair a molecular curvature workflow for reaction-path analysis

A chemistry group is replaying a small, archived curvature calculation while
checking a high-energy molecular reaction path.  The supplied molecular
geometry and electronic-structure output are valid, and the archived record
contains finite numeric values, but the local curvature used
for vibrational and transition-state analysis is not recovered as a complete
scientific object.

Run the offline reproduction, read the accompanying method material, and study
the complete source snapshot.  Repair the implementation so that valid
curvature outputs are represented consistently for supported molecular sizes
and valid calculations.  The repair must generalize to other molecules, matrix
dimensions, and valid calculations; do not hard-code the supplied geometry,
matrix, eigenvalues, or report.

Work only in this task directory.  The evaluation environment has no network
access.  You may modify files under `source/`; do not modify the task
statement, public reproduction, fixtures, or evaluation infrastructure.

Run the diagnostic with:

```bash
python reproduce.py
```
