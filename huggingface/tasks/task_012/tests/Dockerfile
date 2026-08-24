ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-012:v0.1.0@sha256:3ccc8ecdaed2fce6d60b926a927315995930a3f75a1713470564b11f2622e47c
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
