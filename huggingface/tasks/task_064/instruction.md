# Task 064

Run the supplied offline reproduction first:

```bash
python reproduce.py
```

Then inspect the real calculation log, the supplied scientific method note, the common data model, and the parser workflow. The visible symptom is a finite but scientifically inconsistent energy interpretation, not a parser crash. Determine which records in the program output describe the same physical calculation and how an optional pairwise correction should participate in the canonical result.

Repair the source snapshot under `source/`. Keep the public API usable for callers that use the normal top-level parser entry point. The implementation should generalize across supported output versions and calculation modes of the supplied program family: equivalent scientific quantities may appear more than once in a calculation, and one logfile may contain more than one ordered calculation record.

Your change must preserve the documented sign and unit conventions, keep records associated with their calculation, and leave ordinary calculations without the optional contribution unchanged. Do not hard-code the supplied molecule, input filename, output values, or one exact line layout. Do not modify the fixture to hide the symptom and do not bypass the parser with a task-specific script.

Use the supplied paper note and source documentation as the offline scientific references. You may add small local tests while investigating, but the final repair should be in the source library rather than in `reproduce.py`.
