ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-102:v0.1.2@sha256:cea5dd0c726e5914a0f50cad96ec82c27b2666aa19558fcfb6edc5a5f48c0891
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
