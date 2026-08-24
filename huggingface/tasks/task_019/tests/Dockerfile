ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-019:v0.1.2@sha256:1929078137bb6eaee21666521ad9dfe4759c2f6bfa40459e70f7b1c6a1389566
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
