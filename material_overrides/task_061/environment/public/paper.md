# Scientific context: celestial reprojection and mosaicking

This task studies how a celestial image is reprojected into a target WCS and
combined without confusing surface brightness, pixel solid angle, and flux.
The explanation below is benchmark-authored context; it is not a copy of a
publisher article.

## References

- Greisen, E. W. and Calabretta, M. R., "Representations of celestial
  coordinates in FITS", *Astronomy & Astrophysics* 395 (2002), 1061-1075,
  DOI: <https://doi.org/10.1051/0004-6361:20021327>.
- Event Horizon Telescope Collaboration, "First M87 Event Horizon Telescope
  Results. IV. Imaging the Central Supermassive Black Hole", *The
  Astrophysical Journal Letters* 875, L4 (2019), DOI:
  <https://doi.org/10.3847/2041-8213/ab0e85>.

The local text extraction of the EHT article is distributed under CC BY 3.0.
Its attribution and conversion notice are in `paper_assets/README.md`. The
WCS article PDF and text conversion are not bundled because no redistribution
grant was identified; its DOI above is the canonical source.

## Method notes

For an input image with surface-brightness units, a reprojection changes the
pixel footprint on the sky. A flux comparison therefore has to account for
the input and target pixel solid angles and for the returned footprint mask.
The supplied FITS files are deterministic benchmark fixtures, not an
observational dataset.
