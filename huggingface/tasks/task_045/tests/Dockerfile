ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-045:v0.1.1@sha256:8f1017124bd8c6ff303864a9f681042f38a68c6026620b1ddc187bfba8555525
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
