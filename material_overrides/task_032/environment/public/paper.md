# Primary research and method material

This task concerns GROMACS nonbonded topology import in a historical OpenMM
snapshot. The following sources provide the broad scientific and format
context:

1. **OpenMM 7: Rapid development of high performance algorithms for molecular
   dynamics**, <https://doi.org/10.1371/journal.pcbi.1005659>. The article is
   dedicated to the public domain under CC0 1.0. It is linked rather than
   copied because the publisher's complete HTML page also contains site code
   and page chrome outside the scientific article.
2. **GROMACS reference manual: non-bonded interactions**,
   <https://manual.gromacs.org/current/reference-manual/functions/nonbonded-interactions.html>.
3. **GROMACS reference manual: topology file formats**,
   <https://manual.gromacs.org/current/reference-manual/topologies/topology-file-formats.html>.
4. The OpenMM documentation distributed with the source snapshot under
   `source/docs-source/`.

The GROMACS pages are linked rather than copied. The two supplied topology
representations and coordinates were authored specifically for this benchmark
from arbitrary synthetic parameters. They contain no third-party force-field
parameter set. Their mathematical equivalence follows from
`C6 = 4 epsilon sigma^6` and `C12 = 4 epsilon sigma^12`.

The source tree, synthetic inputs, public workflow, and linked original
references are sufficient to investigate the version-specific importer
behavior offline.
