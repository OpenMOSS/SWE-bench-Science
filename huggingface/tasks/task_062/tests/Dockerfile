ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-062:v0.1.1@sha256:9be82d475502b1a517ae673d1a02040204f092cc7e698303b97467504804e7a5
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
