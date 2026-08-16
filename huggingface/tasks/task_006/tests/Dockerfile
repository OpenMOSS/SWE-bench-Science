ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-c-task-006:v0.1.0@sha256:0be098de5952eeccd310f68602f806dbe7c39b8dedd1c8965d2f98b299e243c0
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
