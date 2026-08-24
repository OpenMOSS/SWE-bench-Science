ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-071:v0.1.2@sha256:8a0331f79ccb899160037fed3c654e0ced230d08a60af652c8f941d3544077d7
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
