# Restore the scientific meaning of an exported orbital history

A mission-analysis workflow starts from a valid osculating two-body state and
exports a bounded history for event analysis and visualization. The supplied
historical scientific-software snapshot completes the export, but downstream
users report that the physical meaning of the resulting history is not
consistent with the definitions in the supplied scientific material.

Use the complete paper, the official project documentation in `source/`, the
full source snapshot, the fixture, and the project-native summaries produced by
the public reproduction to investigate the inconsistency and repair the
implementation.

Keep the repair focused on the documented semantics of an orbit-history export:
the exported history must remain a faithful time-indexed representation of the
same physical two-body motion. The behavior must generalize beyond the supplied
numbers to valid supported inputs while preserving the existing public API and
other documented ways of creating an ephemeris. Do not hard-code the fixture,
workflow output, or filenames, and do not alter generated reports.

Do not modify the supplied fixture or generated reports. Do not hard-code the
public input, workflow output, or filenames. A successful repair should make
the scientific representations mutually consistent, not merely suppress an
exception or change the public report.

Run the offline scientific reproduction while investigating:

```bash
python reproduce.py
```

The source snapshot is intentionally pre-fix. The public command is an
execution smoke test: both the untouched and repaired source should be able to
produce the documented artifacts, while infrastructure failures are reported
separately. The public case is only one legal input; the repair must generalize
and must not depend on the public report or a particular patch shape.
