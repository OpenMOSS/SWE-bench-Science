ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-081:v0.1.2@sha256:23307e6b40dc1829749c4a3e0fafb4f0985a161b3e6a2872ca25050af222367a
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
