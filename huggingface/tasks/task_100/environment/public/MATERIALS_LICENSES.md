# Auxiliary Material Licenses

Audit date: `2026-08-16`

Public redistribution requires explicit permission; third-party exceptions are evaluated separately.

This task requires explicit restricted-license opt-in.

Reason: The upstream AuToGraFS snapshot has unresolved LGPL-2.1 versus MIT declarations; only the retained code and independently generated synthetic data are distributed under explicit restricted opt-in.

## `environment/repo/src/autografs`

- Kind: `reduced_source_snapshot`
- Distribution decision: `restricted`
- License: `LGPL-2.1-family and MIT (upstream conflict)`
- Source: <https://github.com/DCoupry/autografs/tree/c2f22341f2b1eb2f619b76534cf4abe2e5e6b3a3>
- Copyright: AuToGraFS contributors; conflicting upstream license files retained
- Modified or converted: `yes`
- Third-party exceptions: The task is restricted until the upstream conflict is resolved.

## `environment/repo/src/autografs/data/topologies.json.gz and defaults.xyz`

- Kind: `benchmark_authored_synthetic_library`
- Distribution decision: `bundled`
- License: `MIT`
- Source: <https://github.com/OpenMOSS/SWE-bench-Science>
- Copyright: OpenMOSS SWE-bench Science contributors
- Modified or converted: `yes`
- Third-party exceptions: No RCSR, IZA, PORMAKE, ToBaCCo, CoRE MOF, or article-derived data.

## `environment/repo/src/autografs/data/uff4mof.py`

- Kind: `benchmark_authored_geometric_constants`
- Distribution decision: `bundled`
- License: `MIT`
- Source: <https://github.com/OpenMOSS/SWE-bench-Science>
- Copyright: OpenMOSS SWE-bench Science contributors
- Modified or converted: `yes`
- Third-party exceptions: Independent approximate values; not the UFF4MOF table.
