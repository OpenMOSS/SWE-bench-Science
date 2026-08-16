ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-002:v0.1.0@sha256:8cbc3c732b8b98f2715f99738209013c0caca2fb1ff9c0b7f5e211036b1e80eb
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
