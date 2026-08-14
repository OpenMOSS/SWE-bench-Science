# Complete the edge-graph scientific capability

The source tree is a real intermediate snapshot from the development of an
atomistic-model backend. It contains the first public data contract for a
`NeighborGraph`, but the surrounding scientific capability is incomplete.

A downstream model must be able to start from atom coordinates and, for both
ordinary and periodic systems, construct a graph whose edges represent the
neighbor displacements used by the potential-energy model. The same graph must
remain usable when the number of edges is padded for a compiled/static backend.
Per-edge energy derivatives must then be transformed into per-atom forces,
per-atom virials, and one virial for each frame. Empty frames, isolated atoms,
virtual atoms, periodic-image neighbors, and padded guard edges are all valid
scientific situations rather than exceptional test-only cases.

Inspect the source context, run `python reproduce.py`, and
complete the reusable capability under `source/`. Preserve the public data
contract where it is already meaningful, and keep the implementation usable
with NumPy and the array-API style used by the source snapshot.

The package-level public API for the completed capability is explicit. Export
these names from `deepmd.dpmodel.utils` (the implementation may live in any
module under `deepmd/dpmodel/utils/`):

- `build_neighbor_graph`
- `from_dense_quartet`
- `node_validity_mask`
- `segment_sum` and `segment_mean`
- `edge_force_virial`

The file layout is your choice; hidden verification checks these public
behaviors through the package namespace rather than requiring a particular
internal module split.

The derivative contract is also part of the public behavior. For
`edge_vec = r_src - r_dst` and `g = dE / d(edge_vec)`, use

```text
F_k = sum(g for edges with dst=k) - sum(g for edges with src=k)
edge_virial = -outer(g, edge_vec)
```

Attribute a complete edge virial to its source atom, ignore masked guard edges,
and return one `(3, 3)` virial per frame. Reject non-positive cutoffs and
inconsistent coordinate, type, or cell shapes with `ValueError` rather than
silently producing an empty or misaligned graph.

The result must be a coherent workflow, not a fixture-specific patch. It must
support more than the public coordinates, more than one frame, and more than
one edge count. Do not hard-code atom indices, distances, edge counts, force
values, or a particular periodic cell. Keep the sign and tensor-layout
conventions explicit in code and documentation so a downstream model can rely
on them.

The public reproduction is only a starting point. A successful solution must
also preserve ordinary non-periodic behavior while adding the missing general
scientific cases.
