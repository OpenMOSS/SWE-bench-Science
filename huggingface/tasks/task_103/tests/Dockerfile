ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-103:v0.1.1@sha256:f5aee22839b572d8edf7c7884c1473cca47f07ee681bd11309ad3fd71d26c6dc
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
