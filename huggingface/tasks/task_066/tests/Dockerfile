ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-066:v0.1.2@sha256:e0c5e2586296c77af23f4dd662cec8b6d4e0e21078e5a2ceb453930f1cd60654
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
