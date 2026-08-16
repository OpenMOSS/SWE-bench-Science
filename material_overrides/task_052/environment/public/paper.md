# Scientific material for the FiPy study

> **NIST attribution and change notice.** The bundled finite-volume chapter
> and polycrystal example come from FiPy, a work of the U.S. National Institute
> of Standards and Technology, source commit
> `11e5c6ae26207a60e223d46473ac364b352ac982`. They are not subject to
> copyright in the United States and are republished courtesy of NIST. The
> files are copied unchanged from `docs/source/numerical/discret.rst` and
> `examples/phase/polyxtal.py`; this surrounding overview was prepared by
> SWE-bench Science. NIST does not endorse this benchmark.

## Primary software-method paper

Jonathan E. Guyer, Daniel Wheeler, and James A. Warren, “FiPy: Partial
Differential Equations with Python,” *Computing in Science & Engineering*,
11(3), 6-15 (2009).

- DOI: <https://doi.org/10.1109/MCSE.2009.52>
- Official FiPy citation record: `source/docs/source/PUBLICATIONS.rst`

FiPy is an object-oriented partial differential equation solver based on the
cell-centered finite-volume method. Its documented applications include
diffusion, convection, phase-field models, electrochemistry, and evolving
materials microstructure.

## Version-matched original method material

The complete finite-volume method chapter shipped with this source version is
provided without task-specific annotations at:

`paper_assets/finite_volume_method.rst`

The chapter defines the mesh in terms of cells, faces, and vertices; derives
the control-volume forms of transient, convection, diffusion, and source terms;
and explains how face areas, face normals, cell volumes, and distances between
neighboring cell centers enter the discretization.

The corresponding source tree also contains the same chapter at
`source/docs/source/numerical/discret.rst` and the full package documentation
and docstrings relevant to mesh and variable behavior.

## Complete upstream phase-field example

FiPy's upstream polycrystalline solidification example is provided at:

`paper_assets/polycrystal_phase_field_example.py`

It is a full scientific example rather than a benchmark-specific excerpt. It
models coupled temperature, phase, and crystal-orientation fields and includes
the governing equations. The example describes orientation as an angular field
on a circle and uses spatial gradients in the phase and orientation dynamics.

## Supporting phase-field reference

Jonathan E. Guyer, W. J. Boettinger, J. A. Warren, and G. B. McFadden, “Phase
field modeling of electrochemistry I: Equilibrium,” *Physical Review E* 69,
021603 (2004), DOI <https://doi.org/10.1103/PhysRevE.69.021603>.

## General finite-volume identities

For a cell-centered control volume (V_P), the transient contribution uses the
cell measure:

\[
\int_{V_P} \frac{\partial(\rho\phi)}{\partial t}\,dV
\simeq
\frac{\rho_P(\phi_P-\phi_P^{old})V_P}{\Delta t}.
\]

Using the divergence theorem, a flux divergence becomes a sum over cell faces:

\[
\int_{V_P} \nabla\cdot(\mathbf{u}\phi)\,dV
\simeq
\sum_f (\mathbf{n}\cdot\mathbf{u})_f\,\phi_f\,A_f.
\]

For diffusion, the normal derivative between adjacent cell centers (P) and
(A) is approximated with their physical separation:

\[
(\mathbf{n}\cdot\nabla\phi)_f
\simeq
\frac{\phi_A-\phi_P}{d_{AP}}.
\]

These definitions apply to valid nonuniform as well as uniform orthogonal
meshes. The per-cell dimensions determine the physical domain and the local
geometric factors used by the discrete operators.

## Periodic orientation fields on a finite-volume mesh

The phase-field example uses an orientation variable whose values are angles.
An angle is not an ordinary real number: values that differ by one full turn
represent the same state. Let

\[
  W(a) = ((a + \pi) \bmod 2\pi) - \pi
\]

denote the representative chosen for one angle difference. The important
point for a finite-volume implementation is that the quantity to which `W`
is applied must have the same meaning as an angle difference. A cell-centered
gradient is not the first quantity produced by the Gauss construction.

For a control volume \(P\), first form the surface-integrated vector

\[
  \mathbf{I}_P =
  \sum_{f \in \partial P}
  s_{P,f}\, A_{P,f}\, \mathbf{n}_{P,f}\, q_f,
\]

where \(A_{P,f}\) is the measure of the face, \(\mathbf{n}_{P,f}\) is its
outward normal, \(s_{P,f}\) is the cell-face orientation, and \(q_f\) is the
face representation of the angular field. The ordinary cell gradient is then

\[
  \mathbf{g}_P = \frac{\mathbf{I}_P}{V_P}.
\]

The distinction matters because \(\mathbf{I}_P\) carries a face measure,
whereas \(\mathbf{g}_P\) has units of angle per length. Applying a nonlinear
periodic map after an arbitrary rescaling is not equivalent to applying it
before that rescaling. In general,

\[
  \frac{a}{V_P} W\!\left(\frac{\mathbf{I}_P}{a}\right)
  \ne
  \frac{b}{V_P} W\!\left(\frac{\mathbf{I}_P}{b}\right)
\]

for two nonzero face-measure scales \(a\) and \(b\). The equality only
appears in special uniform cases where the different geometric quantities
happen to collapse to the same constant. In three dimensions, substituting a
length for a face measure is additionally dimensionally inconsistent: the
surface integral carries area units, not length units.

For the angular finite-volume reconstruction, introduce one scalar
\(\bar A_P\) that represents the active face measure of the control volume.
This scalar is not a coordinate spacing or a tunable numerical parameter. It
must be symmetric under a permutation of the active faces, depend linearly on
their measures with equal weight for each active face, and reduce to the common
face measure when all active faces are equal. Those requirements lead to the
arithmetic mean of the active face measures:

\[
  \bar A_P =
  \frac{1}{N_P}\sum_{f \in \partial P} A_{P,f},
\]

where \(N_P\) counts the active faces of \(P\). The periodic operation is
then applied to the dimensionless angle-like quantity obtained from the
surface integral, and the finite-volume units are restored afterwards:

\[
  \mathbf{g}^{\mathrm{periodic}}_P
  = \frac{\bar A_P}{V_P}
    W\!\left(\frac{\mathbf{I}_P}{\bar A_P}\right).
\]

This order preserves three pieces of information at once: the face
contribution used to build the surface integral, the control-volume measure
used to recover a cell gradient, and the period of the angular variable. It
also prevents one coordinate direction from receiving a different modular
interpretation merely because its cell width is different.

### Why an axis spacing is not a face measure

Consider a rectangular two-dimensional cell with widths \(h_x\) and \(h_y\).
The faces normal to the x direction have measure \(h_y\), while the faces
normal to the y direction have measure \(h_x\). In three dimensions the same
relationship becomes \(h_y h_z\), \(h_x h_z\), and \(h_x h_y\) for the three
families of faces. Thus an axis spacing describes a distance across a cell;
a face measure describes the size of the boundary through which a finite-volume
contribution is integrated. They are different geometric objects, even on an
orthogonal mesh.

This difference is invisible on a uniform isotropic grid and can be hidden by
an angular field that never crosses the representative boundary. It becomes
observable when the cell is anisotropic and the field values straddle the
\(-\pi/\pi\) cut. A sound implementation should therefore be checked with
both kinds of limiting case, rather than only by checking that the result is
finite.

### Coupled face, cell, and flux consistency

The face gradient, the cell gradient, and the divergence of a face flux are
three views of the same discrete geometry. For an interior face shared by
cells \(P\) and \(A\), the normal component should use the wrapped angular
difference and the physical center separation:

\[
  (\mathbf{n}\cdot\nabla q)_f
  \simeq \frac{W(q_A-q_P)}{d_{AP}}.
\]

The corresponding control-volume flux must use that same face gradient,
orientation, and face measure:

\[
  D_P = \frac{1}{V_P}
  \sum_{f \in \partial P}
  s_{P,f} A_{P,f}(\mathbf{n}\cdot\nabla q)_f.
\]

Changing only the scalar used during periodic normalization can therefore
make a field look smooth at cell centers while making the face flux and cell
gradient describe different discrete operators. Independent checks should
compare these representations on nonuniform, anisotropic meshes and should
also verify the inverse-length scaling obtained when every physical length is
multiplied by the same factor.
