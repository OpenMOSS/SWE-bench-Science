# Scientific background and permitted local material

This task concerns cross-spectral timing measurements. The following method
papers are cited for scientific context but are **not redistributed** in this
task because their available records do not grant a reusable-content license:

- B. A. Vaughan and M. A. Nowak, "X-Ray Variability Coherence: How to
  Compute It, What It Means, and How It Constrains Models of Cyg X-1 and
  GX 339-4," *The Astrophysical Journal* 474, L43-L46 (1997),
  <https://doi.org/10.1086/310430>, arXiv `astro-ph/9610257`.
- A. Ingram, "Error formulae for the energy-dependent cross-spectrum,"
  *Monthly Notices of the Royal Astronomical Society* 489 (2019),
  <https://doi.org/10.1093/mnras/stz2409>, arXiv `1909.01385`.

## Independent method overview

For two simultaneous time series, divide the observations into independent
segments and compute a Fourier transform for each segment. At a frequency
bin, a cross spectrum can be formed as the product of one transform with the
complex conjugate of the other. Averaging cross spectra over independent
segments or neighboring frequencies reduces the variance while retaining
phase and amplitude information shared by the two signals.

A commonly used squared-coherence estimator compares the squared magnitude
of the averaged cross spectrum with the product of the averaged power spectra.
Measurement-noise contributions have to be treated consistently in the
numerator and denominator. The estimator and its uncertainty therefore depend
on which realizations were averaged, the number of statistically independent
averages, the power-spectrum normalization, and the adopted noise levels.
Changing only one of those conventions can produce internally inconsistent
results even when every intermediate array has a plausible shape.

Energy-dependent products use a subject band and a reference band. If those
bands overlap, correlated counting noise can enter the cross spectrum; a
workflow must apply the same overlap convention to the measured cross powers,
noise correction, and error propagation. Error estimates should be derived
from the same ensemble of segment-level or frequency-level measurements as
the reported average rather than from a differently normalized aggregate.

The historical source snapshot and its ordinary documentation under
`/opt/swebench/source` provide the software context used by the task.

## Redistributed software paper

The task retains one locally redistributed paper:

- Matteo Bachetti et al., "Stingray 2: A fast and modern Python library for
  spectral timing," *Journal of Open Source Software* 9(102), 7389 (2024),
  <https://doi.org/10.21105/joss.07389>.
- Local copy: `paper_assets/stingray2_joss_2024/joss.07389.pdf`.
- Copyright: 2024, the paper authors.
- License: Creative Commons Attribution 4.0 International,
  <https://creativecommons.org/licenses/by/4.0/>.
- Source: <https://joss.theoj.org/papers/10.21105/joss.07389>.
- Change notice: the PDF is redistributed unchanged; this surrounding
  Markdown overview was independently written for SWE-bench Science.

