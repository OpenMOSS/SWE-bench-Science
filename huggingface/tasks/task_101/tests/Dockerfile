ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-101:v0.1.2@sha256:2373e04b521a579f62bfab97e77ec0d135ada7df3dc3b79fac61d708ff346e6d
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
