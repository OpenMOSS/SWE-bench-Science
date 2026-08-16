ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-035:v0.1.1@sha256:3f5829a8aac0f18cc8716f569d96154613a115e082be984153eedf0e81afdc8a
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
