ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-cython-task-016:v0.1.1@sha256:0f5faca298805d01f881ef0b1dbf658995fc725b850452eb5832a1e627272248
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
