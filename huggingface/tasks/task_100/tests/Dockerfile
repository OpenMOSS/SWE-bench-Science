ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-100:v0.1.2@sha256:4363b9caed452c88bf06344867287140d8991b9ced35de0ea78785383653842d
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
