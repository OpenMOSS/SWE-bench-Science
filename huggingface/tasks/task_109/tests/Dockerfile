ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-109:v0.1.1@sha256:b8c2d6a3e9d319f7cb3294afe63976c1bad693e90e7d01980eb7c0c4720cb545
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
