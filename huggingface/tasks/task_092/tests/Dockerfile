ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-092:v0.1.2@sha256:9a77ea43008ece2a97125a1478648bea8d1b0e664be45d95e372db1945fd99d1
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
