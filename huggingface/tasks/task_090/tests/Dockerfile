ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-090:v0.1.2@sha256:76cf7e7a1391b73fc5c739e8713738918e629bca0ba4e9b5c66d1b68f593d783
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
