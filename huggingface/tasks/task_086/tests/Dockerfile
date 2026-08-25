ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-086:v0.1.2@sha256:450167e21dfaf4268961c60697f4e738bb5bf281f174d4afb8a178c9808be945
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
