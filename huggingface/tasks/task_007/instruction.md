Inspect the Suspect source code, run the public
reproduction workflow, and repair the dynamic-registration implementation so
that spectral registration improves drifted magnetic-resonance spectroscopy
transients.

The public reproduction uses a small dynamic MRS-like series. The current
workflow should build or use a common reference, estimate frequency/phase drift
for each transient in the stable spectral region, compensate that drift before
averaging, and keep unusable transients from polluting the reported average.
The reported quality metrics show that the processed series is still not
behaving as a scientifically meaningful drift correction should.

Your repair should be general. Do not hard-code the public fixture, point
count, dwell time, peak frequency, or a fixed set of numeric outputs. The
correct behavior should hold for other drift directions, spectral windows,
noise levels, and sampling settings.

Run:

```bash
python reproduce.py
```

The script writes `outputs/reproduction_report.json` and prints the same report
to stdout.
