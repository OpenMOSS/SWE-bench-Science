# Restore the scientific workflow

A materials-modeling workflow in the supplied FiPy source behaves consistently
on its long-standing control mesh, but the archived polycrystal study cannot
complete when the same coupled finite-volume calculation uses a valid
orthogonal mesh with graded cell sizes. The study cannot produce a usable
phase-field update.

Reproduce the problem with `python reproduce.py`. Read the supplied method
material and inspect the complete source snapshot. Repair the scientific
implementation so that the coupled workflow behaves coherently for the
archived input and for other valid meshes, while preserving existing uniform-
mesh behavior.

Make a general source repair. Do not replace the archived input, bypass the
scientific calculation, or hard-code the public report. The evaluator will run
independent finite-volume studies that are not included in the public payload.
