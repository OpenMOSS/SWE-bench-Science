ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-096:v0.1.1@sha256:8dbb1d8bae6fcea0585e71a28f019d6daa33026072fcb83cad7cd36ed10cbb94
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
