# Scientific source bundle

The archived calculation relies on a standard consequence of periodic
electronic-structure theory: a commensurately sampled primitive cell and its
corresponding enlarged zone-center cell describe the same finite periodic
problem. After normalizing extensive quantities by the number of primitive
cells and matching the numerical model, their converged per-cell results should
agree to the residual numerical tolerance. The public symptom is a violation
of that high-level equivalence, not a diagnosis of an implementation layer.

## Primary references

1. Q. Sun et al., "PySCF: the Python-based simulations of chemistry
   framework," *WIREs Computational Molecular Science* 8, e1340 (2018),
   <https://doi.org/10.1002/wcms.1340>.
2. Q. Sun et al., "Recent developments in the PySCF program package,"
   *The Journal of Chemical Physics* 153, 024109 (2020),
   <https://doi.org/10.1063/5.0006074>.
3. Q. Sun, T. C. Berkelbach, J. D. McClain, and G. K.-L. Chan, "Gaussian
   and plane-wave mixed density fitting for periodic systems," *The Journal of
   Chemical Physics* 147, 164119 (2017),
   <https://doi.org/10.1063/1.4998644>.

The former ar5iv HTML conversions are not bundled. Their arXiv records grant
arXiv a non-exclusive distribution license but do not grant this benchmark a
right to redistribute converted copies, including third-party AIP/ACS figures.

## Original software examples

The Apache-2.0 files `upstream_kpoint_gamma_example.py`,
`upstream_density_fitting_example.py`, and `upstream_fft_cutoff_example.py`
remain available in `paper_assets/`. They establish supported workflows and
expected scientific usage without identifying a repair.
