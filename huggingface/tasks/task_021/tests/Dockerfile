ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-021:v0.1.0@sha256:4556f2a24cf62743731721b1c2e36f82a08ca5c173f639e47b305e93bcd2013d
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
