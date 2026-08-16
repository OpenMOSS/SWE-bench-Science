ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-084:v0.1.0@sha256:8cbe4554c727f25c1584f79c48f574a3d08e1fcf6d3c4cb32df36a7d8482216a
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
