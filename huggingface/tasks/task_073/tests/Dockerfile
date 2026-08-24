ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-073:v0.1.2@sha256:e274f86569446b6a62d7bd1a8a5bf0b272b10361113d6a27d8ef9a1894598928
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
