Inspect the MACS3 source tree and public reproduction. Repair the scientific
peak-refinement workflow so that
valid ATAC-seq candidate regions can be processed together with a sparse
fold-change signal track across legitimate breakpoint and resolution patterns.

Preserve the scientific meaning of genomic interval boundaries, quantitative
scores, and summit locations for ordinary cases. The scored workflow in this
task follows the historical array-backed `bedGraphTrackI` path used by the
upstream regression. The repair must remain valid across nested, adjacent, and
breakpoint-misaligned intervals. Do not hard-code the public chromosome names,
coordinates, values, case names, or output counts.

Within each chromosome, score segments are ordered scientific evidence. Once a
segment's evidence has been consumed by and attributed to a completed refined
peak, it must not be counted or attributed again to a later overlapping or
nested candidate. A candidate with no remaining supporting evidence need not
emit a record. This is a result-level attribution requirement; the traversal,
state representation, and implementation strategy are intentionally left open.

Run `python reproduce.py` from this task directory to build the local MACS3
runtime and inspect the public symptom. You may edit the source tree and run
the reproduction repeatedly. Do not add generated Cython build products to
your patch.
