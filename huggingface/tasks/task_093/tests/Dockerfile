ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-093:v0.1.1@sha256:6378d5a97c239e8867c6a09fd2a07ec026a7abfb0ddd80bb8bae56f8377408b7
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
