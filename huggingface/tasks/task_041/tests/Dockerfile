ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-041:v0.1.1@sha256:89c3b061bcb5d19a2b28722e4c8a1a5c2435e8641d4cdc2f2ffbd565bc48ff10
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
