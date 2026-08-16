from __future__ import annotations

import json
import math
from pathlib import Path

from workflow.validate_equivalence import calculate_energies


TASK_DIR = Path(__file__).resolve().parent
REPORT_FILE = TASK_DIR / "outputs" / "public_reproduction_report.json"


def write_report(report: dict[str, object], exit_code: int) -> int:
    REPORT_FILE.parent.mkdir(exist_ok=True)
    payload = json.dumps(report, indent=2, sort_keys=True, allow_nan=False) + "\n"
    REPORT_FILE.write_text(payload, encoding="utf-8")
    print(payload, end="")
    return exit_code


def main() -> int:
    try:
        energies = calculate_energies()
        finite = all(math.isfinite(value) for value in energies.values())
        equivalent = finite and math.isclose(
            energies["combination_rule_1"],
            energies["combination_rule_3"],
            rel_tol=1.0e-10,
            abs_tol=1.0e-10,
        )
    except Exception as exc:  # Infrastructure failures are a separate state.
        return write_report(
            {
                "schema_version": "1.0",
                "status": "runner_failure",
                "error_type": type(exc).__name__,
                "error": str(exc),
            },
            2,
        )

    return write_report(
        {
            "schema_version": "1.0",
            "status": "workflow_completed" if equivalent else "pre_fix_expected_failure",
            "observation": {
                "finite": finite,
                "equivalent": equivalent,
            },
        },
        0 if equivalent else 1,
    )


if __name__ == "__main__":
    raise SystemExit(main())
