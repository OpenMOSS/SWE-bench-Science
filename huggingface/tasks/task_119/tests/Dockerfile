ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-119:v0.1.2@sha256:713fe383e429decf0fd25a51115c41c09b2c865f90d8a345ab21386d2e84303b
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
