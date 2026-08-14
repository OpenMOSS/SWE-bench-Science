# Complete the Native Multi-Equilibrium TERPSICHORE Workflow

The supplied source is a substantial DESC-native migration of a three-dimensional
ideal-MHD stability workflow. It can load and represent several equilibrium
families, and it contains lower-level geometry, spectral, operator, solver, and
energy components. It does not yet provide one complete and trustworthy native
workflow for a researcher who submits a new supported VMEC/DESC equilibrium.

Inspect the source and run:

```bash
python reproduce.py
python reproduce.py --check
```

The public reproduction uses the same high-level input path for an axisymmetric
control equilibrium and a genuinely three-dimensional equilibrium. It reports
whether each end-to-end native calculation completes and records the resulting
finite stability scalars without inferring a repair location from internal
source structure. A candidate scientific-chain exception or non-finite result
is reported only as a coarse scientific failure; fixture, path, import, and
dependency failures are reported separately as runner failures.

Complete the implementation so that supported stellarator-symmetric equilibria
can traverse this scientific workflow through one native path. The implementation
must preserve the meaning of intermediate quantities and remain general across
equilibrium metadata, field periods, spectral content, and discretization.

Your implementation will be evaluated on additional equilibria, resolution and
mode changes, a full-domain vacuum/wall configuration, and an unsupported
asymmetric representation that must be rejected explicitly.

Do not:

- hard-code fixture names, dimensions, field periods, arrays, or final scalars;
- use precomputed comparison arrays as inputs to the production calculation;
- call the external TERPSICHORE executable as the implementation;
- make a report claim success when an upstream scientific stage is unavailable;
- silently discard asymmetric Fourier content;
- solve only the public cases or only the final growth-rate scalar.

The task workspace and fixtures are available offline. The goal is capability
completion, not a local text or branch patch.
