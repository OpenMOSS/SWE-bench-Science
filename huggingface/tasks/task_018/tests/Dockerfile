ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-cython-task-018:v0.1.0@sha256:8b1dd5120cf838ae85b5b2824d2d9fdf419b830b49127d10e3c0d34ef38ead8e
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
