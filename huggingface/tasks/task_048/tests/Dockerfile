ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-048:v0.1.2@sha256:2f9f66bb675f3e67c8ece3caa9a5ddf155534dbf656e0fd1d5f4d2c58c886500
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
