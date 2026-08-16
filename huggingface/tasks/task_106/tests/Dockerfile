ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-106:v0.1.1@sha256:2c7ddddb4e5595efd5421461fffab8a15fd94618104523a27a6f3bbba6e71a26
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
