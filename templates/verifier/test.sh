#!/bin/sh
set -eu

mkdir -p /logs/verifier
cd /app/task___TASK_ID__
git config --global --add safe.directory /app/task___TASK_ID__
git reset --hard HEAD
git clean -ffdqx

patch=/logs/artifacts/model.patch
if [ -s "$patch" ]; then
    git apply --binary "$patch"
fi

exec python /tests/grader.py
