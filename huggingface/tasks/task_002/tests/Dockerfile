ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-002:v0.1.0@sha256:a863b98f920e1e9b1aede8bd0460d039628aab19a413cce3dad7417028e1bd1a
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
