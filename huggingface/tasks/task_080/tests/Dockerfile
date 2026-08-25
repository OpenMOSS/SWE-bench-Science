ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-080:v0.1.2@sha256:f888e89324368b7223fcf04994b08f31984fda060871bc80bf512e1cdb2c0bf6
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
