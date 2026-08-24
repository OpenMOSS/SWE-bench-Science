ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-055:v0.1.2@sha256:93596c6ca11f7ee7e015a4cb0fcb08f92346756f3bc945b5732e387fd6fd2ed0
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
