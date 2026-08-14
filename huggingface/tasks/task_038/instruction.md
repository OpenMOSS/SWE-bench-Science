# Stable classification of archived crystal records

A materials-data pipeline imports a small archived batch containing two legal
representations of the same periodic Ag/O structure.  Both records are finite
and processable, but the final batch summary is not stable under the change of
representation.

Run the public reproduction, inspect the complete C source and public
observation, and repair the implementation so that physically equivalent crystal
records retain one classification through ordinary import and batch analysis.
The repair must generalize to other structures, lattice settings, origins, and
operation orderings; do not special-case the supplied files, coordinates,
species, or output token.

Work only in this task directory.  The evaluation environment is Linux and has
no network access.  You may modify files under `source/`.  Do not replace the
scientific calculation with a fixed report.

Use:

```bash
python reproduce.py
```

The command returns `1` for the reproduced finite scientific inconsistency,
`0` after a successful repair, and `2` for a build or runner failure.  The
public report intentionally contains only a project-level batch observation.
