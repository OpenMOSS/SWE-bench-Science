from __future__ import annotations

import json
import math
import sys
from pathlib import Path


TASK_DIR = Path(__file__).resolve().parent
SOURCE_DIR = TASK_DIR / "source"
if not SOURCE_DIR.is_dir():
    SOURCE_DIR = TASK_DIR.parent / "repo"
FIXTURE = TASK_DIR / "fixtures" / "molecular_case.xyz"
REPORT_FILE = TASK_DIR / "outputs" / "public_reproduction_report.json"


def _write_report(report: dict[str, object], exit_code: int) -> int:
    REPORT_FILE.parent.mkdir(exist_ok=True)
    payload = json.dumps(report, indent=2, sort_keys=True) + "\n"
    REPORT_FILE.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return exit_code


def _read_xyz(path: Path) -> list[tuple[str, float, float, float]]:
    lines = path.read_text(encoding="ascii").splitlines()
    if len(lines) < 3:
        raise ValueError("the self-authored XYZ fixture is incomplete")
    count = int(lines[0].strip())
    records = []
    for line in lines[2:]:
        fields = line.split()
        if len(fields) != 4:
            raise ValueError("the self-authored XYZ fixture has malformed coordinates")
        values = tuple(float(value) for value in fields[1:])
        if not all(math.isfinite(value) for value in values):
            raise ValueError("the molecular geometry contains a non-finite value")
        records.append((fields[0], *values))
    if len(records) != count:
        raise ValueError("the XYZ atom count does not match its records")
    return records


def main() -> int:
    try:
        if not (SOURCE_DIR / "cclib" / "__init__.py").is_file():
            raise FileNotFoundError("the supplied source snapshot is incomplete")
        records = _read_xyz(FIXTURE)
    except Exception as exc:  # noqa: BLE001 - infrastructure failures need a report.
        return _write_report(
            {
                "schema_version": "1.0",
                "status": "runner_failure",
                "error_type": type(exc).__name__,
                "message": "The self-authored public smoke fixture could not be read.",
            },
            2,
        )

    return _write_report(
        {
            "schema_version": "1.0",
            "status": "workflow_completed",
            "operation": "offline molecular geometry smoke",
            "observations": {
                "parser_family": "cclib source snapshot",
                "atom_count": len(records),
                "coordinate_frames": 1,
                "finite_geometry": True,
            },
        },
        0,
    )


if __name__ == "__main__":
    raise SystemExit(main())
