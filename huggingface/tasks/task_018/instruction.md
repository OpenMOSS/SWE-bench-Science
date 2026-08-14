# Repair a scientifically inconsistent HMMRATAC workflow

The supplied directory contains a pinned snapshot of MACS3, including the real
HMMRATAC implementation used to infer accessible chromatin from ATAC-seq
fragments. The offline reproduction exposes an unexpected behavior: adding a
genomic exclusion mask can change model-input statistics and derived behavior on
chromosomes that are not covered by the mask.

Inspect the HMMRATAC documentation in `source/` and the complete
fragment-to-model call graph, and repair the implementation so the exclusion mask
has the intended scientific meaning throughout the workflow. The repair must work
for ordinary paired-end fragment data and count-bearing single-cell fragment data,
preserve half-open interval semantics, and keep count and barcode bookkeeping
consistent for count-bearing fragment data.

Duplicate retention and duplicate-related CLI naming are intentionally outside
the scope of this task. Preserve the existing duplicate policy and do not add,
remove, rename, or reinterpret duplicate flags. Repeated coordinates in the
fixtures are there to verify that blacklist filtering preserves the existing
record multiplicity and count/barcode associations.

This is a capability repair, not a fixture-specific patch. Do not hard-code the
public chromosomes, coordinates, lengths, counts, or expected outputs. Preserve
the existing public workflow and keep all generated files under `outputs/`.

Run the public reproduction with:

```bash
python reproduce.py
```

Treat the supplied case as one observation of the workflow defect. The repair
must preserve the documented scientific and record-association semantics for
other valid inputs supported by the same production paths.
