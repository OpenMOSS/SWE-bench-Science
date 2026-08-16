ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-091:v0.1.1@sha256:ec8f7cd03251aa71c0c771816e9833c0daec737c669dc482635be41873933529
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
