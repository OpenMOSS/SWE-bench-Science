ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-013:v0.1.2@sha256:1777aaef426fe23edda9c2e7f536877678a48ddd9d4d4a2c90e6520d8a6144af
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
