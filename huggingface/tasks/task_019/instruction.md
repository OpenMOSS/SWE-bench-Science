# Complete robust topic-to-cistrome binarization

The included pycisTopic source can turn topic distributions attached to a full
cisTopic model into selected cell or region sets. A downstream workflow now
needs to consume probability matrices exported independently from topic-model
training and produce the discrete topic sets used for motif enrichment and
cistrome construction.

The current source does not complete that workflow reliably. The public
reproduction exercises both region-topic and cell-topic inputs, including
zero-heavy probabilities at the precision used by exported matrices. It reports
that the required topic sets or portable output artifacts cannot be produced
consistently.

Inspect the source snapshot and fixtures, and complete the
scientific capability so that independent topic-probability matrices can be
validated, optionally smoothed, thresholded, ranked and exported without a full
in-memory cisTopic object.

Requirements:

- support matrices whose rows are named cells or genomic regions and whose
  columns are topics;
- preserve name-to-score alignment and deterministic descending ranking;
- support top-n selection and the histogram-based thresholding methods already
  documented by the source;
- remain numerically finite for zero-heavy `float32` topic probabilities;
- treat constant topics as having no separable evidence rather than selecting
  every row because of a histogram artifact;
- reject duplicate names, non-finite values, invalid `ntop` bounds and malformed
  genomic intervals;
- produce the required portable downstream artifacts, including
  deterministic threshold tables, cell tables and BED-compatible region tables;
- retain the existing object-based entry point where practical;
- do not hard-code the public names, topic count, matrix shape or expected
  selected sets.

Run the public workflow with:

```bash
python reproduce.py
```

The benchmark runs offline. Generated files belong under `outputs/`.
