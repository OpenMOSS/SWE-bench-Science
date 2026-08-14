# Restore multidimensional NMR acquisition grids

A multidimensional NMR acquisition can arrive as a compressed FID stream plus a
sparse coordinate schedule. Study the source snapshot and the public
reproduction. Repair the package so that valid acquisition workflows preserve
that schedule alongside the compressed stream in both eager and low-memory
reader paths, and so the public processing workflow can restore the compressed
rows into a full multidimensional acquisition grid without losing the declared
acquisition and quadrature layout. Preserve ordinary fully-sampled behavior.
The repair must generalize when valid layouts, dimensions, direct FID lengths,
dtypes, and sampling patterns change.

Do not hard-code the supplied observations or replace the NMR data model with a
fixed answer. Work only under this task directory. The evaluation environment is
offline; all required Python dependencies and source files are provided.

Run the public diagnostic with:

```bash
python reproduce.py
```

The command returns `0` when the diagnostic report is produced and `2` for an
import, dependency, path, or other runner failure. The public report is a
workbench signal; final evaluation performs independent scientific consistency
checks on broader cases.
