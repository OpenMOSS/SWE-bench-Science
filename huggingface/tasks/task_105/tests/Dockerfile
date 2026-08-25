ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-cpp-task-105:v0.1.2@sha256:bde966ff804c2d2b43f0b4e82e3b72ee1c713d8c7d6e19d7799d2d5fd1c31923
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
