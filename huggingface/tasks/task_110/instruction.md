# Restore consistent cross-section analysis results

A structural-analysis team is reviewing several valid connected cross-section
models. Normal meshing and engineering analyses complete with finite reports.
The supplied laboratory also derives each model's ordinary first moments of
area directly from its constructed outline. For material-bearing models, the
package's ordinary first-moment result is finite but incompatible with that
construction observation, without clearly reporting that the requested result
is unavailable. Results carried through ordinary workflows therefore cannot be
interpreted consistently in downstream beam calculations and research records.

Reproduce the laboratory, inspect the supplied source and complete scientific
material, and repair the implementation so that ordinary result requests do
not silently return a physically incompatible quantity. Preserve valid analysis
and reporting behavior throughout supported workflows. The repair must
generalize beyond the supplied laboratory: do not special-case its geometry,
values, case labels, or printed output, and do not replace calculations with
fixed results.

Work only under this task directory. The evaluation environment is Linux and has no network access. You may modify files under source/; do not modify the task statement, public evidence, or reproduction workflow.

Run the public laboratory with:

~~~bash
python reproduce.py
~~~

A finite first-moment result that is incompatible with its construction observation
reports `pre_fix_expected_failure` and exit code 1. After every model either reports a
matching first moment or explicitly reports that the ordinary result is unavailable, the
laboratory reports `post_fix_success` and exit code 0. `runner_failure` and exit code 2
identify an execution problem rather than a scientific conclusion.

For this public laboratory, an explicitly unavailable ordinary result is reported by a
`RuntimeError` or `ValueError` with a nonempty explanation. Other unexpected exceptions
remain execution failures.
