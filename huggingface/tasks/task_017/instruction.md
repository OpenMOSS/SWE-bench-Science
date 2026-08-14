# Repair a scientific dark-matter map workflow

This task contains a pinned source snapshot of Gammapy and an offline
reproduction of a dark-matter line-of-sight calculation. A map that is valid
for a small field of view becomes unusable for a wider field, and calculations
that do complete must still represent the intended astrophysical integral.

Inspect the relevant source documentation and call graph, then repair the
implementation so that the dark-matter spatial calculation remains
scientifically valid across the supported geometries, profiles, units, and
annihilation/decay modes.

The goal is one general scientific repair. Preserve the existing public API and
do not hard-code the public map, a particular profile, an angular width, a
matrix shape, or expected numerical values. Keep the repair inside the source
snapshot and do not modify the test harness.

Run the public symptom reproduction with:

```bash
python reproduce.py
```

The evaluator is offline. Do not download catalogs, query remote services, or
depend on a local absolute path. Generated reports belong under `outputs/`.
