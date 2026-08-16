ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-082:v0.1.0@sha256:a829af72c8e716a904d83a590a865d07a7b9a31a8d4b7083afbf90b6611a937c
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
