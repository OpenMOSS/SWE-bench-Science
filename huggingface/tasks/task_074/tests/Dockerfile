ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-074:v0.1.2@sha256:15fcd5df916db5181d6b4b90803bf534d6bbf07af4d9b8dbea4da69e6ad9bc8d
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
