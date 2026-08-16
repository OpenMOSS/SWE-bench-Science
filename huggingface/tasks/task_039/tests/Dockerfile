ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-039:v0.1.1@sha256:1533cb3577d15acdc7fd3b1f755f8c4ec80fbb528b7bcb6bcf918c6559f20e4a
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
