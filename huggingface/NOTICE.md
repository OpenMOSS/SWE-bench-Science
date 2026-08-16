# SWE-bench Science Notices

The root `LICENSE` applies to the project-owned release tooling and documentation
in this repository, unless a file states otherwise.

Task metadata, task instructions, upstream source snapshots, dependencies, and
Docker image contents may be derived from third-party projects. They remain under
their original licenses and are not relicensed by the root MIT license. The
canonical per-task license, provenance URL, and license gate are recorded in
`huggingface/data/tasks.csv` and each task metadata file.

The release boundary intentionally excludes complete source snapshots, private
tests, graders, reference solutions, model patches, credentials, and run logs
from GitHub and the Hugging Face thin snapshot. Full task source is used only by
the local build staging workflow and by the corresponding Docker image build.

For GPL/LGPL/AGPL-family and academic non-commercial task images, the image
build must preserve the upstream license and notice files. The
`--allow-restricted-licenses` option selects those tasks for materialization; it
is not a substitute for the applicable license obligations.

## Task-Specific Material Provenance

Tasks 076-090 do not redistribute article or supporting-information PDFs. The
paper references in their public notes are citations, not bundled copies.

- Task 084 includes selected ABACUS relaxation test fixtures from
  `deepmodeling/dpdata`. The source commits and reorganization note are recorded
  in `fixtures/PROVENANCE.md` inside the environment image; the files remain
  LGPL-3.0-or-later.
- Task 085 includes 16 C/H/N/O files from the official MIO 1-1 v1.1.0 parameter
  release. They are byte-identical to the release files and remain CC BY-SA
  4.0; the full license and attribution are bundled with them.
- Task 089 uses a benchmark-authored synthetic ORCA-style text fixture. No ORCA
  output, manual content, publication data, or upstream discussion values are
  redistributed by that fixture.

Task 083 excludes the unrelated upstream methane tutorial that cited a book
chapter and linked an externally hosted figure. It is not needed to build or
evaluate the task.
