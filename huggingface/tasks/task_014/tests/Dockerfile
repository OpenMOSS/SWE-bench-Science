ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-014:v0.1.0@sha256:9d4ec1597ff0ea20e8355f790a4d8fcb0198dec12a7ccfefe6a18cdd205b7362
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
