# Complete Support for the New Stability Cases

The source snapshot implements a native Python path for a TERPSICHORE-style
ideal-MHD stability calculation. It already supports the established cases, but
the three supplied research cases use another valid perturbation convention
and do not produce the expected scientific behavior.

Run:

```bash
python reproduce.py
```

Inspect the Python source and task context, and complete the missing scientific
capability. The result must work across all supplied kinetic regimes and must
preserve behavior for the existing convention.

Do not hard-code case names, fixture values, or final diagnostics. Internet
access is unavailable during evaluation.
