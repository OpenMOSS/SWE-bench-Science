ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-082:v0.1.2@sha256:2a854eb9e7b25e025056eb83a35d0e44dedd2bc360bc4ad4a09689ad13f81796
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
