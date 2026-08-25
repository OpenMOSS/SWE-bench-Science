ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-117:v0.1.2@sha256:ef7f9de0ec866088427b5f419696b4b962b953e7d3452184470660aeb7795a0d
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
