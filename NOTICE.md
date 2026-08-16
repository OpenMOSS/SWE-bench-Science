# SWE-bench Science Notices

The root `LICENSE` applies to the project-owned release tooling and documentation
in this repository, unless a file states otherwise.

Task metadata, task instructions, upstream source snapshots, dependencies, and
Docker image contents may be derived from third-party projects. They remain under
their original licenses and are not relicensed by the root MIT license. The
canonical per-task license, provenance URL, and license gate are recorded in
`huggingface/data/tasks.csv` and each task metadata file.

Auxiliary papers, documentation copies, figures, notebook outputs, and
scientific fixtures are reviewed independently from the source snapshot. Their
source URLs, licenses, copyright notices, modifications, third-party
exceptions, and distribution decisions are recorded in
`manifests/materials.jsonl` and in each audited task's `MATERIALS.json` and
`MATERIALS_LICENSES.md`. An item marked `excluded` is not present in a
published task image.

Tasks that remove, replace, crop, or clear bundled material to eliminate its
bytes are rebuilt from a clean context. A Docker whiteout layer is not treated
as removal because bytes in an older distributed layer remain recoverable.

The release boundary intentionally excludes complete source snapshots, private
tests, graders, reference solutions, model patches, credentials, and run logs
from GitHub and the Hugging Face thin snapshot. Full task source is used only by
the local build staging workflow and by the corresponding Docker image build.

For GPL/LGPL/AGPL-family and academic non-commercial task images, the image
build must preserve the upstream license and notice files. The
`--allow-restricted-licenses` option selects those tasks for materialization; it
is not a substitute for the applicable license obligations.
