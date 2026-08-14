# Restore physical consistency in a calibrated cell measurement workflow

I am validating a quantitative-phase microscopy workflow. The supplied image
is a real cell image, and the workflow segments it and measures the resulting
region through the project's ordinary measurement API. The same kind of object
can be represented on a sampling grid whose intervals are different along the
two image axes. The program completes, but the resulting shape record is not
consistent with the physical-coordinate interpretation described by the
provided scientific material.

Please inspect the supplied method paper, the image-data reference, the source
snapshot, and the public reproduction. Determine why the calibrated
measurements are inconsistent and repair the source so that the scientific
behavior is correct for valid inputs in general. Preserve the public API and
backwards-compatible behavior for ordinary unit sampling. The repair must work
for other masks, intensities, dimensionalities, coordinate origins, and valid
sampling intervals; do not hard-code the supplied image, threshold, dimensions,
or recorded output values.

The public command is:

```bash
python reproduce.py
```

The public reproduction is only a workflow smoke test over one complete
measurement record. Use it to inspect the project behavior, then trace the
complete scientific computation and validate your repair on new inputs.
