# Task 063

A population-genetics consortium is auditing two frozen exports of the same
cohort after a routine archive-curation operation. Both exports load, pass the
project's structural validation, retain the same samples and recorded
genealogical relationships, and produce finite reports. However, the inferred
population-history profiles disagree even though the curation was intended to
preserve the represented scientific study.

Run the supplied offline audit, then investigate both exports, the historical
source, original papers, and supplied documentation. Repair the scientific
implementation under `source/` so that the ordinary cohort workflow is
consistent with the documented tree-sequence model. The repair must generalize
to other valid tree sequences and supported population-history analyses.

Do not replace either export, hard-code this cohort, or bypass the workflow.
The public reproduction is one end-to-end diagnostic case; the scientific
behavior must generalize beyond it.

Run:

```bash
python reproduce.py
```
