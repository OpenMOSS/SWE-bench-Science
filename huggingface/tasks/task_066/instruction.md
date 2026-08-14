# Repair an inconsistent regional climate-validation workflow

A climate-data group is validating a regional precipitation event against the
supplied station observations. The model field loads, remains finite, and has
the expected shape, but the completed regional validation is inconsistent with
the observations. The supplied model and station files are valid inputs for
this workflow.

Run the public reproduction, study the supplied CF and project material, and
inspect the complete historical source snapshot. Repair the implementation so
that the scientific workflow behaves consistently for valid inputs rather than
only the supplied case.

Do not hard-code the supplied dimensions, values, file name, or report outcome.
Do not modify the fixture, task statement, workflow, or evaluation
infrastructure. Work only under this task directory and modify the source
snapshot as needed.

Run the public smoke test from the task root with:

```bash
python reproduce.py
```

The untouched source is expected to produce a finite but inconsistent
scientific result. A correct repair should make the public validation
consistent. Import, fixture, dependency, and unrelated execution failures must
remain distinct from the scientific result.
