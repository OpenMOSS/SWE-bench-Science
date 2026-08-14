# Task

I prepare crystal-structure input files for an external structure
prediction and refinement workflow that reads SHELX/AIRSS `.res` files
(using the documented format contract). I convert my structures to
`.res` with the supplied source snapshot (`source/`), and before
submitting the files I validate them against the format requirements.

For the structure in `fixtures/public/structure.json`, the export
completes without any error, and when I read the produced file back with
the same library I get exactly my structure back — but my format
validation still rejects the file: the atom records' species references do
not all resolve, through the file's own SFAC species list, to the elements
named in those records, so any conforming external tool would misread or
reject it.

You can reproduce this with:

```bash
python reproduce.py
```

See `reproduction.md` for the report contract.

Please inspect the source and its format handling, figure out why the
produced files violate the required format, and repair the
implementation so that the `.res` files it produces conform to the format
for all valid inputs — any composition, any number of species and sites,
ordered or partially occupied sites, and structures carrying site spin
moments. The produced files must also be stable: exporting the same
structure must give the same file every time. Do not hard-code specific
structures, species, orderings, or expected file contents.
