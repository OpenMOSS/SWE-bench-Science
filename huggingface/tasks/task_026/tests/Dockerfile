ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-026:v0.1.1@sha256:46fadf320df6b6adca39a81c2e83a3f16f8fa486a2adfefdc56a0518edb5db45
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
