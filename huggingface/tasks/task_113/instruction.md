# Repair an inconsistent solar-resource workflow

Inspect the supplied historical `pvlib` source snapshot and run the public
diagnostic. A fixed-site solar-resource calculation receives valid
timezone-aware timestamp series whose labels differ even though they describe
the same sampling instants. The calculation returns different physical
estimates for the two representations.

Repair the implementation so equivalent valid aware representations produce
consistent observable solar-resource outputs and so the change generalizes to
supported scalar/series inputs and fixed-offset or named time zones. Preserve
public API shapes, output labels, and documented behavior for valid inputs
outside the observed discrepancy.

Supported aware inputs in this task include pandas `Timestamp` and
`DatetimeIndex` values with fixed-offset or named time zones, in both scalar and
series forms. Parsing ambiguous or nonexistent naive local times is outside
the task scope.

The supplied diagnostic is one small fixed-site clear-sky case. Your change
must generalize beyond those timestamps and values; do not special-case the
sample or hard-code any reported result.

Keep the task offline and deterministic. Modify implementation code under
`source/` only. Do not edit `reproduce.py`, the paper material, generated
reports, or supplied data assets.
