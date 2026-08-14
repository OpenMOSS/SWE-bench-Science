# SWE-bench Science Notices

The root `LICENSE` applies to the project-owned release tooling and documentation
in this repository, unless a file states otherwise.

Task metadata, task instructions, upstream source snapshots, dependencies, and
Docker image contents may be derived from third-party projects. They remain under
their original licenses and are not relicensed by the root MIT license. The
canonical per-task license, provenance URL, and GPL-family gate are recorded in
`huggingface/data/tasks.csv` and each task metadata file.

The release boundary intentionally excludes complete source snapshots, private
tests, graders, reference solutions, model patches, credentials, and run logs
from GitHub and the Hugging Face thin snapshot. Full task source is used only by
the local build staging workflow and by the corresponding Docker image build.

For GPL/LGPL/AGPL-family task images, the image build must preserve the upstream
license and notice files. The `--allow-GPL` option selects those tasks for
materialization; it is not a substitute for the applicable license obligations.
