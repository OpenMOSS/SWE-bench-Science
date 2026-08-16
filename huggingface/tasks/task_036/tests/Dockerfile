ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-036:v0.1.1@sha256:97009f66b48e65e82d8e706d3e07eadded40d4918020554f7a9886708786dd69
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
