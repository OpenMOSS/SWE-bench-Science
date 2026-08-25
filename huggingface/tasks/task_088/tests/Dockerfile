ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-088:v0.1.2@sha256:3905c31661704748245f173b67234e4cd7f57b7a1e313eb289004adfeef588ed
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
