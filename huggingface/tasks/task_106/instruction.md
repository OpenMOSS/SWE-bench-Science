# Reproduce and extend a version-pinned MAP4/MAPC retrieval protocol

You are working in a chemoinformatics codebase used to reproduce and extend a
published molecular-space retrieval benchmark. A methods-validation group has
re-run a small part of the workflow using an upstream peptide benchmark input
and a version-pinned MAP4/MAPC method contract. The current source snapshot
does not complete the requested offline observation.

Run the public workbench first:

```text
python reproduce.py
```

Treat its output as experimental evidence from a failed methods reproduction.
Use it together with the complete source snapshot, the raw benchmark input,
and the unmodified versioned method documents in `paper_assets/` to determine
which scientific behavior is not being preserved and repair the implementation.
The reference panel and query panel must remain comparable under the documented
protocol when the workflow is repeated or extended.

Do not use the network or add a dependency. Do not special-case the benchmark
rows, expected output values, or report file. The implementation should
generalize to other molecules, widths, seeds, input orders, storage modes, and
stereochemical inputs covered by the public API.
