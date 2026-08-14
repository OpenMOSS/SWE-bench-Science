# Repair inconsistent celestial image representation in a mosaic

A calibrated FITS cutout is being placed onto a different valid celestial grid
and combined through the project's documented conservative mosaicking
workflow. The operation completes and the generated arrays are finite, but the
source measurement and resolved image are not consistent with the scientific
meaning that the accompanying material assigns to this representation change.
The target frame covers the supplied cutout; this is not an out-of-bounds or
missing-data case.

Use the complete source snapshot, the supplied scientific material, the FITS
fixtures, and the public reproduction to investigate the inconsistency. Repair
the implementation so that supported celestial images and WCS representations
preserve the documented scientific meaning of the data.

Do not modify the supplied fixtures or generated reports. Do not hard-code the
public image, its dimensions, sky position, pixel values, WCS coefficients, or
the observed disagreement. Preserve documented public behavior and the APIs
used by existing workflows.

Run the smoke reproduction before and after your changes:

```bash
python reproduce.py
```

The command reports the scientific observation rather than deciding whether a
repair is correct; use the measurements together with the supplied method
material and the complete source.

After changing the supplied package source, rebuild it before rerunning the
reproduction:

```bash
cd source
python setup.py build_ext --inplace
cd ..
```
