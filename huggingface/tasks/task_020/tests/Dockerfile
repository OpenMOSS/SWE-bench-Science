ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-020:v0.1.1@sha256:373d19decc97090d881cd8c39d3e9b8eeb9481ec4f7d2dfdda10b29ec11b92f6
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
