ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-059:v0.1.0@sha256:2dda66b63502d81c2e09a7b0311ca76b3796dc1cd28349f9ece060a35795c8b0
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
