# Repair inconsistent lateral-frame member observations

A structural-engineering group is replaying a small lateral-load frame used to
compare alternative bracing layouts for earthquake and wind resilience.  The
model is valid, the nonlinear analysis completes, and the node and member
quantities are finite.  However, one supported member report is not consistent
with the geometry implied by the solved frame, and the scalar and sampled forms
of that report do not agree.

Run the offline reproduction, inspect the complete source snapshot and the
accompanying official project material, and repair the implementation so that
supported frame analyses report physically consistent member observations.  The
repair must generalize to other valid geometries, member orientations, load
signs, unilateral-element states, physical-member subdivisions, and public
result-query paths.  Preserve ordinary active-member force, bending, and
second-order behavior.

Do not hard-code the displayed frame, member names, node displacements, or
reported values.  Do not modify the task statement, public reproduction,
scientific material, or evaluation infrastructure.  Work only under this task
directory and keep the workflow offline.

Use:

```bash
python reproduce.py
```

The command writes a finite JSON observation report under `outputs/`.  Its
`workflow_completed` status means that the scientific workflow ran and exposed
surface observations; it is not the final correctness decision.
