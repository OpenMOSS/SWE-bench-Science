ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-042:v0.1.1@sha256:2d3c7dba05b8ca04b80900872baa59a5f3bc42d765e80ed58aa917bf0126c512
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
