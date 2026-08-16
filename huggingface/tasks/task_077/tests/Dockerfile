ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-077:v0.1.0@sha256:f9f3eb576dd41c94b0407e0a0395e1df75d6cad627be53a028bc995d4f66e633
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
