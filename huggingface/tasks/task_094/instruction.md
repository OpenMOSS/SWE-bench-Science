# Repair magnetic-space-group operations across archived settings

A materials archive stores magnetic symmetry records contributed by data
producers using their own coordinate conventions.  The public diagnostic record
resolves to a finite magnetic operation family, but downstream archive consumers
cannot rely on this retained source to preserve the scientific meaning of valid
records across producer conventions.

Run the public reproduction, inspect the source and public workflow, and repair
the implementation so that archived magnetic records retain their scientific
operation semantics across supported producer conventions.  The repair must
generalize beyond the supplied record.  Do not replace the magnetic symmetry
calculation with fixed outputs, special-case the supplied BNS number, or change
the public reproduction to hide a failure.

Work only under this task directory.  The evaluation environment is Linux and
has no network access.  You may modify files under `source/`; do not modify the
task statement, reproduction, fixtures, workflow, or evaluation infrastructure.

Run the public smoke test with:

```bash
python reproduce.py
```

The command returns `0` when the diagnostic workflow completes and writes a
finite report, and `2` for a runner or environment failure.  The public report
is a workbench observation, not the final correctness oracle.
