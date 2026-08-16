# Auxiliary Material Licenses

Audit date: `2026-08-16`

Public redistribution requires explicit permission; third-party exceptions are evaluated separately.

## `environment/repo`

- Kind: `source_snapshot`
- Distribution decision: `bundled`
- License: `BSD-3-Clause`
- Source: <https://github.com/cclib/cclib/tree/593f0d67cf6a76f4a047f9a4856125c05947cff4>
- Copyright: cclib contributors; LICENSE retained
- Modified or converted: `no`
- Third-party exceptions: Notices retained with source.

## `environment/public/fixtures/molecular_case.log`

- Kind: `vendor_program_output`
- Distribution decision: `excluded`
- License: `LicenseRef-ORCA-No-Redistribution-Grant-Found`
- Source: <https://orcaforum.kofo.mpg.de/>
- Copyright: ORCA and its contributors; output contains an All rights reserved notice
- Modified or converted: `no`
- Third-party exceptions: Removed from the public environment and retained only as a verifier-side private fixture.

## `environment/public/fixtures/molecular_case.xyz`

- Kind: `benchmark_authored_smoke_fixture`
- Distribution decision: `bundled`
- License: `MIT`
- Source: <https://github.com/OpenMOSS/SWE-bench-Science>
- Copyright: OpenMOSS SWE-bench Science contributors
- Modified or converted: `yes`
- Third-party exceptions: Self-authored geometry for public parser smoke execution; not an ORCA output.
