Inspect the BEDTools source tree and the public reproduction workflow. A small genomic interval-enrichment analysis becomes unstable when the database/background interval set is augmented with valid intervals that cannot overlap the query intervals.

Those appended background intervals should not create new observed overlaps, but they are still part of the statistical sample used by the Fisher exact test table. Repair the implementation so that interval-enrichment output uses complete summary state for valid BED and genome inputs. The fix should preserve the behavior of ordinary interval-overlap commands and should not hard-code the public fixture, file names, chromosome names, counts, p-values, or coordinates.

Run `python reproduce.py` from this task directory to build the local source and reproduce the public failure.
