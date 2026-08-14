# Repair an inconsistent tandem-mass spectral similarity workflow

A mass-spectrometry group is comparing a small library of complete tandem mass
spectra using the historical `matchms` source snapshot supplied with this
task. The workflow finishes and returns finite values, but the resulting
similarity matrix is not consistent with the scientific interpretation of an
entropy-based MS/MS similarity: a self-comparison is not a reliable reference
point, and the aggregate scores can leave the valid similarity range.

Run the offline reproduction, inspect the complete source snapshot and the
scientific references, and repair the implementation so the public similarity
workflow agrees with the method definition for valid tandem spectra. The
repair must remain correct for other molecular spectra, mass tolerances, and
the project's pairwise and matrix calculation routes. Preserve the existing
public API and keep the implementation usable for large library comparisons.

Do not hard-code the supplied molecules, the displayed aggregate values, a
single peak list, or a filename-specific result. Do not modify the supplied
scientific inputs or generated reports.
