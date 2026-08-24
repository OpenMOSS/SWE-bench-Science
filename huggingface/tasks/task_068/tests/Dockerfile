ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-c-task-068:v0.1.2@sha256:edbc641c9a63d8696b6ab6be1acfd67cc29ec5a6a32bfecb672a3bf9e9f5bbbb
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
