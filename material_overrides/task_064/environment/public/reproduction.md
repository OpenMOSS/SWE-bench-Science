# Public reproduction

Run `python reproduce.py` from this directory. The public smoke uses the
small, benchmark-authored `fixtures/molecular_case.xyz` geometry so that no
vendor program output is redistributed. It checks the source snapshot boundary
and finite coordinate semantics only.

The authentic ORCA output needed for the broader parser behavior tests is kept
inside the verifier image under `private_tests/fixtures/`. It is not part of
the public task environment.
