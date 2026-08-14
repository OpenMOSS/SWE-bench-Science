# Repair inconsistent finite-volume operations on a connected multi-face grid

An ocean-modeling group is post-processing a tracer field from a global
finite-volume calculation. The supplied grid is represented as several
logically rectangular faces that meet at rotated edges. Interpolation and
differencing across those edges are part of the same diagnostic workflow used
to form transport and mixing budgets.

The workflow completes and returns finite arrays, but a connected padding call
can reorder the local dimensions. Values occupying the expected connected-halo
positions then no longer come from the neighboring face declared by the
cubed-sphere topology. The result can also depend on process-level ordering
even though the physical grid and field are unchanged. A connected edge is a
geometric interface: padding must preserve the input dimension order, and for a
scalar face-label field every non-corner halo position in that layout must have
the label of the declared neighboring face, independent of process hash seed.

Inspect the complete source snapshot, the finite-volume references, the grid
description, and the public reproduction. Repair the implementation so that
connected-face operations are geometrically consistent for valid inputs
supported by the project. The repair must remain correct for other connected
multi-face grids, fields, widths, orientations, and valid scientific workflows,
not only for the supplied probes.

Do not hard-code the supplied field, face count, process seeds, edge probes,
array values, or fixture path. Do not change the scientific input or public
report to hide a failure. Preserve existing behavior for ordinary single-face
grids and valid disconnected boundaries.

Run `python reproduce.py` before and after your repair. The command checks a
small, transparent subset of connected edges by deriving each required
neighbor directly from the public `face_connections` table. It also reports a
dimension-order comparison as a non-authoritative observation. Hidden tests
cover the complete topology and broader field and operation families, so the
public observations are not the complete correctness oracle.
