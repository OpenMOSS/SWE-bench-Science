# Scientific source material

The redistributable article bundled with this task is:

- Atsushi Togo, Kohei Shinohara, and Isao Tanaka, *Spglib: a software library
  for crystal symmetry search*, *Science and Technology of Advanced Materials:
  Methods* 4 (2024), <https://doi.org/10.1080/27660400.2024.2384822>.
- Local copy: `paper_assets/spglib_2024_cc_by.pdf`.
- License: Creative Commons Attribution 4.0 International,
  <https://creativecommons.org/licenses/by/4.0/>.
- Repository record: <https://mdr.nims.go.jp/pid/c45f8c83-c091-407e-a7e4-758dd34f559b>.

The earlier arXiv PDF, ar5iv conversion, and derived figures were removed
because the arXiv record did not grant this benchmark a Creative Commons
redistribution license.

The supplied source snapshot also contains upstream project documentation at
`source/docs/`, the public C interface at `source/include/spglib.h`, citation
metadata at `source/CITATION.cff`, and the project bibliography at
`source/docs/references.bib`.

The two CIF fixtures are representation adaptations of Crystallography Open
Database entry 1509692, <https://www.crystallography.net/cod/1509692.html>,
which is dedicated to the public domain under CC0 1.0. Classification labels
were removed; geometry, symmetry expressions, sites, and cell parameters were
retained.

Several coordinate descriptions can represent the same physical crystal.
When a basis or origin changes, all representation-dependent quantities must
be transformed coherently. The article, project documentation, public
interface, runnable observation, and implementation should be read together;
they do not prescribe a repair route.
