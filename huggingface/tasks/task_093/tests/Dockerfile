ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-093:v0.1.2@sha256:6ec6749f5e92805d41c3c0ab03069ac84f48685692331d1b55a18f3b5d2b6374
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
