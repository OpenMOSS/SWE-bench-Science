ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-c-task-006:v0.1.2@sha256:3cc0295af4cc108d28acc43a0586aaecba16f76952070c6bd12319007300cb33
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
