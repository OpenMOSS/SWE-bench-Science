ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-029:v0.1.2@sha256:e517cabd9151676fb17dc610d9eebc3ae1415fdc99e98b990c1b7cae904235c1
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
