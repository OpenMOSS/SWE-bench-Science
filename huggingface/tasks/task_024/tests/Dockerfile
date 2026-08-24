ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-024:v0.1.2@sha256:9d9cfe8d89db5c5597bc9ef83f7eef9e4497ef7b26f2bef8e93be9644293e80a
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
