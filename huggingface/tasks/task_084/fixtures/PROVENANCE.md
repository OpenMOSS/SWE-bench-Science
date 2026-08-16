# Fixture Provenance

The ABACUS relaxation fixtures in this directory are selected from the
`deepmodeling/dpdata` test suite and remain under dpdata's
LGPL-3.0-or-later license. The complete license text is preserved in
[`../source/LICENSE`](../source/LICENSE).

- `abacus_relax_normal`, `abacus_relax_abnormal`, and
  `abacus_relax_nostress` come from dpdata commit
  [`80abfc5037876c0e883dcb58cd96521397e3fe36`](https://github.com/deepmodeling/dpdata/commit/80abfc5037876c0e883dcb58cd96521397e3fe36),
  under `tests/abacus.relax`.
- `abacus_relax_case` comes from dpdata commit
  [`0b6bf2f75f58e87fe07b0989772c7fe00fdcd3c9`](https://github.com/deepmodeling/dpdata/commit/0b6bf2f75f58e87fe07b0989772c7fe00fdcd3c9),
  which introduced the regression case used by the task.

The benchmark reorganizes the selected files into task-specific fixture
directories but does not alter their scientific values. `abacus_relax_case.json`
is benchmark-authored metadata describing the selected regression fixture.
