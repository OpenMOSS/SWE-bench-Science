ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-067:v0.1.1@sha256:c89861f5ff214b94dfb9407e7c40d85343f1b7a0d07437d96078249abd4c909c
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
