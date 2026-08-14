# Repair spin-model consistency in DeePMD-kit

Inspect the paper and source code, run the reproduction workflow, and repair the
implementation so the public spin calculation remains consistent across the
dense and lower layouts exercised by the fixture.

The public workflow uses a few small padded spin systems. It reports aggregate
responses for changes applied to padded batch entries and for control changes
applied to ordinary spin-carrying entries, across both NumPy and Torch
backends. The repair should generalize beyond the particular atom ordering,
padding position, layout, backend, and output mode used by the public run.
