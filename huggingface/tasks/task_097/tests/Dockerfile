ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-097:v0.1.2@sha256:9ff80c8ac79cf51239232c647bc5db7d332781418f76c4400cf57e88b6a4029b
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
