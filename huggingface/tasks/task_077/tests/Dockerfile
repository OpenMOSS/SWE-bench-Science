ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-077:v0.1.1@sha256:eb936b5b0a6db0add7ea609d3b1e2fa52c2fe210e8cc32e301b66ce3221d9051
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
