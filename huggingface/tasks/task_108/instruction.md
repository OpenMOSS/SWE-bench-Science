# Restore stable Jacobi theta evaluations across difficult regimes

The task-local `source/` tree contains a snapshot of mpmath. Work only inside that source tree.

An offline reproduction script reports Jacobi theta observations for valid complex inputs. Some calls either fail to produce a value for legal inputs, or become unstable when the same mathematical quantity is repeated at higher working precision.

Repair the implementation so these theta evaluations are stable for legal inputs and continue to support all four Jacobi theta kinds and derivatives with respect to `z`.

Run:

```bash
python reproduce.py
```

The public workflow is diagnostic and intentionally small. It should keep running offline and producing a finite JSON report after your repair.
