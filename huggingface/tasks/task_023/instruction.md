# Restore continuous periodic trajectories in changing cells

You are repairing a scientific trajectory-analysis workflow in the supplied
MDAnalysis source snapshot. The workflow is used to remove artificial jumps
caused by periodic boundary wrapping before quantities such as mean-square
displacement and diffusion are calculated.

The current implementation behaves inconsistently for valid constant-pressure
molecular-dynamics trajectories whose periodic cell changes with time. In
particular, a trajectory can contain a physically continuous path but the
transformed result can retain a box-length jump. The same physical type of
motion can produce different results under different valid frame schedules,
even though the numerical motion obeys the method assumptions.

Inspect the complete source snapshot and run
`python reproduce.py`. Repair the implementation so that the external
trajectory behavior follows the required variable-cell semantics for changing
orthorhombic and triclinic cells. The correction must work for
general atom counts, cell changes, and crossing directions; do not hard-code the
public coordinates or a single frame index.

Preserve ordinary fixed-cell trajectories, the existing handling of missing or
singular periodic cells, and the diagnostic behavior for non-sequential frame
access. The transformation must also remain coherent when a
trajectory is traversed more than once through the normal MDAnalysis API.

The public reproduction is only a small smoke diagnostic. Use the source call
graph to determine the complete behavior that needs to be repaired. Do not use the network or add external data files. Keep changes
limited to the scientific implementation and any focused tests or comments
that are necessary for a general fix.
