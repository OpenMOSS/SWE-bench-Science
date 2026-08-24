ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-009:v0.1.0@sha256:73746f77074cfc0a1b7abaebf7f95d877a883a454eb8e4e48ef5db52c5ccceac
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
