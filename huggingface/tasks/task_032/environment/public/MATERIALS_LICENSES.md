# Auxiliary Material Licenses

Audit date: `2026-08-16`

Public redistribution requires explicit permission; third-party exceptions are evaluated separately.

This task requires explicit restricted-license opt-in.

Reason: The OpenMM source snapshot includes LGPL-covered CUDA and OpenCL platform components and therefore requires explicit restricted-license opt-in.

## `environment/repo`

- Kind: `source_snapshot`
- Distribution decision: `restricted`
- License: `MIT AND LGPL-family AND BSD-3-Clause`
- Source: <https://github.com/openmm/openmm/tree/d2f76949b3ccac1139f0a0a0d1459aa47e2f0a98>
- Copyright: 2008-2025 Stanford University, the OpenMM authors, and named third-party contributors; notices retained in docs-source/licenses/Licenses.txt
- Modified or converted: `no`
- Third-party exceptions: CUDA/OpenCL platforms are LGPL-covered; additional third-party notices remain bundled.

## `environment/public/fixtures/combination_rule_1.* and combination_rule_3.*`

- Kind: `benchmark_authored_synthetic_scientific_fixtures`
- Distribution decision: `bundled`
- License: `MIT`
- Source: <https://github.com/OpenMOSS/SWE-bench-Science>
- Copyright: OpenMOSS and SWE-bench Science contributors
- Modified or converted: `no`
- Third-party exceptions: Arbitrary benchmark-selected parameters; no third-party force-field parameter set is included.

## `environment/public/paper_assets/openmm_article.html`

- Kind: `publisher_page_capture`
- Distribution decision: `excluded`
- License: `LicenseRef-Publisher-Page-Chrome-Unverified`
- Source: <https://doi.org/10.1371/journal.pcbi.1005659>
- Copyright: Article authors, PLOS, and page-component rightsholders
- Modified or converted: `yes`
- Third-party exceptions: The scientific article is CC0, but the captured full webpage also contains publisher code and page chrome not established as CC0.

## `environment/public/paper_assets/charmm36m_article.html`

- Kind: `article_copy`
- Distribution decision: `excluded`
- License: `LicenseRef-No-Redistribution-Grant-Found`
- Source: <https://pmc.ncbi.nlm.nih.gov/articles/PMC5199616/>
- Copyright: CHARMM36m article authors and publisher
- Modified or converted: `yes`
- Third-party exceptions: NIH author manuscript status is not a redistribution license.

## `environment/public/paper_assets/gromacs_parameter_files.html and gromacs_topology_file_formats.html`

- Kind: `documentation_copies`
- Distribution decision: `excluded`
- License: `LicenseRef-No-Redistribution-Grant-Found`
- Source: <https://manual.gromacs.org/current/reference-manual/topologies/>
- Copyright: GROMACS documentation contributors
- Modified or converted: `yes`
- Third-party exceptions: Saved pages did not carry a grant permitting this redistribution.
