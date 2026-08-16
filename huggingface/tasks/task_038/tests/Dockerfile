ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-c-task-038:v0.1.1@sha256:4bb7c29ed433773c37de68bad0e425e75710b6709e0beec1b63f0f3691539643
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
