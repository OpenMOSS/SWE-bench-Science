# Scientific background for task 045

This task uses xgcm's finite-volume post-processing model. A physical domain
may be represented by several logically rectangular faces, and variables may
occupy different positions on a staggered grid. Interpolation and differencing
therefore need both the local axis position and the topology connecting one
face to another.

## Finite-volume meaning

Finite-volume methods associate values with cells or cell faces and evaluate
fluxes and differences across shared interfaces. A connected multi-face grid
is one physical domain: an interface shared by two faces must expose the same
physical data from either side after applying the encoded orientation.

For a scalar field, a connection transfers the scalar value and may reverse
the tangential index order when two local axes have opposite orientation. For
a vector component, the same geometric reorientation may also change the
component sign. These are physical-grid properties, not arbitrary array
library choices.

## Why halo values matter

Post-processing code often creates a small halo around each face before a
difference or interpolation. At an interior interface, the halo must contain
the neighboring face's edge values; at an external boundary, the configured
boundary condition applies. A wrong halo can have the expected shape while
producing incorrect transport, divergence, vorticity, or mixing diagnostics.

## Repository manuscript and documentation

`source/paper.md` is the manuscript that the xgcm authors submitted to JOSS
review 2631. The authors withdrew it on 6 October 2020; it was never a JOSS
publication and has no JOSS DOI. It is included as part of the MIT-licensed
xgcm source snapshot, with an explicit publication-status notice. Review
record: <https://github.com/openjournals/joss-reviews/issues/2631>.

The source also includes grid-topology and boundary-condition documentation,
project citation metadata, the original surrounding tests, and the manuscript
bibliography. Outputs were cleared from two documentation notebooks so that
embedded CNRM CMIP6 data under CC BY-NC-SA 4.0 is not redistributed. The
unlicensed PyComodo C-grid images were removed and their surrounding text was
rewritten without reproducing the diagram.

The Arakawa C-grid references cited by the manuscript and the retained source
documentation provide the intended scientific context without prescribing a
source-level repair.
