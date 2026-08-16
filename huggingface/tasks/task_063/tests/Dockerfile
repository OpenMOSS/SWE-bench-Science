ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-c-python-task-063:v0.1.1@sha256:708641d17e5aa0d5ae7bb62948e3c802e2f63e1f5fdc8b6f41c4a90506ab0ee5
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
