# Repair the supplied scientific software

A researcher is sampling a finite field from a spherical curvilinear ocean
model grid with the supplied historical source snapshot. The workflow
completes, but the values along a valid smooth track are not scientifically
consistent with the supplied workflow.

Reproduce the behavior, inspect the project source and task workflow, and
repair the implementation so that supported calculations are scientifically
consistent. The repair must generalize beyond the public case and must preserve
normal behavior for other supported grid configurations.

Work only inside this task directory. You may modify files under `source/` and
other task-local implementation files when justified. Do not replace the
scientific workflow with fixed fixture outputs or special-case the public
track. The final answer is the patch produced from your workspace.

Run the public check with:

```bash
python reproduce.py
```
