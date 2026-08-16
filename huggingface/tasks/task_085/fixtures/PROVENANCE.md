# Fixture Provenance

The small `archive_*` inputs are benchmark-authored examples for exercising the
DFTB+ archive workflow.

The `params/mio-1-1` directory contains an unmodified subset of the MIO 1-1
Slater-Koster parameter set: the ordered C, H, N, and O pair files needed by the
examples. Every included file is byte-identical to the corresponding file in
the official
[`mio-1-1.tar.xz` v1.1.0 release](https://github.com/dftbparams/mio/releases/tag/v1.1.0)
published by the DFTB parameter project under
[CC BY-SA 4.0](https://creativecommons.org/licenses/by-sa/4.0/). The complete
license text shipped with the downloaded parameter set is preserved at
[`params/mio-1-1/LICENSE`](params/mio-1-1/LICENSE).

The benchmark selected only the listed element-pair files and changed their
directory placement; it did not change the parameter values. DFTB+ source code
is separately licensed under LGPL-3.0-or-later, while DFTB+ manual content is
CC BY-SA 4.0, as recorded in [`../source/LICENSE`](../source/LICENSE).
