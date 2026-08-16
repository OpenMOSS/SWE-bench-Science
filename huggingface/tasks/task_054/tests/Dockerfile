ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-054:v0.1.1@sha256:9b8eb137609838bf28828e687f9d0814b79c50f67e47fac66478944a2ff5572c
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
