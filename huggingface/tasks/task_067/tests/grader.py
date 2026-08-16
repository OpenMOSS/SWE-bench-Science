#!/usr/bin/env python3
from __future__ import annotations

import json
import os
import subprocess
import sys
import xml.etree.ElementTree as ET
from pathlib import Path


TASK_ID = "task_067"
TASK_ROOT = Path("/app") / TASK_ID
LOG_ROOT = Path("/logs/verifier")
LOG_ROOT.mkdir(parents=True, exist_ok=True)
env = os.environ.copy()
env.update(
    {
        "SCI_BENCH_TASK_ID": TASK_ID,
        "SCI_BENCH_TASK_DIR": str(TASK_ROOT),
        "PYTHONPATH": f"{TASK_ROOT}:{TASK_ROOT / 'source'}",
    }
)


def execute(command: list[str], cwd: Path) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        command,
        cwd=cwd,
        env=env,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=False,
    )


public = execute([sys.executable, "reproduce.py"], TASK_ROOT)
junit = LOG_ROOT / "junit.xml"
# Private tests are a task-owned directory. Their filenames are intentionally
# unconstrained; pytest discovers every supported test module recursively.
private = execute(
    [
        sys.executable,
        "-m",
        "pytest",
        "-q",
        f"--junitxml={junit}",
        "/tests/private_tests",
    ],
    TASK_ROOT,
)

private_total = private_passed = private_failed = 0
if junit.is_file():
    root = ET.parse(junit).getroot()
    suites = [root] if root.tag == "testsuite" else root.findall(".//testsuite")
    private_total = sum(int(suite.attrib.get("tests", "0")) for suite in suites)
    private_failed = sum(
        int(suite.attrib.get("failures", "0"))
        + int(suite.attrib.get("errors", "0"))
        for suite in suites
    )
    private_passed = max(private_total - private_failed, 0)

reward = int(public.returncode == 0 and private.returncode == 0)
summary = {
    "reward": reward,
    "task_id": TASK_ID,
    "public": {
        "passed": int(public.returncode == 0),
        "collected": 1,
        "return_code": public.returncode,
    },
    "private": {
        "passed": private_passed,
        "collected": private_total,
        "failed": private_failed,
        "return_code": private.returncode,
    },
}
(LOG_ROOT / "reward.json").write_text(json.dumps(summary, indent=2) + "\n")
(LOG_ROOT / "reward.txt").write_text(f"{reward:.1f}\n")
(LOG_ROOT / "ctrf.json").write_text(
    json.dumps(
        {
            "reportFormat": "CTRF",
            "specVersion": "0.0.0",
            "results": {
                "summary": {
                    "tests": private_total,
                    "passed": private_passed,
                    "failed": private_failed,
                },
                "tests": [],
            },
        },
        indent=2,
    )
    + "\n"
)
combined = (
    "== public ==\n"
    + (public.stdout or "")
    + "\n== private ==\n"
    + (private.stdout or "")
)
(LOG_ROOT / "test-stdout.txt").write_text(combined)
(LOG_ROOT / "run.log").write_text(combined)
print(json.dumps(summary, sort_keys=True))
