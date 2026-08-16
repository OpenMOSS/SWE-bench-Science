ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-115:v0.1.1@sha256:1b16ce929f12ec92e01fef2775b3ab0d9d96346c3b1a8362ab9559fecc4871f0
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
