# Restore a stereo-preserving tautomer workflow

A cheminformatics workflow uses the supplied RDKit C++ source snapshot to
canonicalize tautomeric forms on a molecule that already carries stereochemical
annotations. One compact V3000 input loads successfully, but the
canonicalization step does not complete.

Run the public reproduction, inspect the source snapshot and the bundled
references, and repair the implementation so that this workflow completes on
the supplied input and remains coherent on other stereo-bearing molecules. Do
not hard-code the fixture, the generated probe, or the public report.

Work only under this task directory. The evaluation environment is Linux,
offline, and provides a C++ compiler, CMake, and Boost headers. You may modify
files under `source/`.

Run the public diagnostic with:

```bash
python reproduce.py
```
