# Repair Local Study Workflow

You are working with a local snapshot of `anndata`, a Python package for
annotated single-cell data matrices. A small offline workflow under `fixtures/`
 and `workflow/` processes multiple local study shards from the same experiment.

Run the public workbench:

```bash
python reproduce.py
```

Users have reported inconsistent behavior when the workflow output is passed
into later analysis steps. The public workbench runs a compact observation pass
over the local result. Repair the local source so the workflow produces
reliable outputs for small and large studies.

Keep the fix inside `source/`. Do not modify the public fixtures, reproduction
script, or task metadata. Your repair should generalize beyond the supplied
files and should remain practical on larger studies.

Do not hard-code values derived from the supplied inputs. Do not download
external data or use network access; all information needed for the public
workbench is already in this task directory.
