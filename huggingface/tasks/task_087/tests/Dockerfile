ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-087:v0.1.2@sha256:c1e7ce200b679565a86e0a7e6de0e562986335d40f81b50c14d0d941f4f962d3
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
