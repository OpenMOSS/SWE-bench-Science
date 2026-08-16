# Public reproduction

Run from the task directory:

```bash
python reproduce.py
```

The command imports two benchmark-authored GROMACS topologies that encode the
same nonbonded model using combination rules 1 and 3. It evaluates both at the
same coordinates on OpenMM's deterministic CPU Reference platform and writes
`outputs/public_reproduction_report.json`.

The report records only whether both observations are finite and equivalent:

- `pre_fix_expected_failure`, exit code `1`: import completed, but equivalent
  inputs did not preserve the same physical result.
- `workflow_completed`, exit code `0`: the two representations agree.
- `runner_failure`, exit code `2`: the runtime or an input could not be loaded.

This pair is a smoke test. The implementation must remain correct for other
valid combination rules, parameters, labels, declaration orders, and explicit
pair terms.
