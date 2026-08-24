ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-fortran-task-051:v0.1.2@sha256:9c3ffb87798fcce875b2c1583c48823f46063d0ccc18ed062e4caf9e35fa8e3c
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
