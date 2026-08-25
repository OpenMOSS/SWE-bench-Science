ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-096:v0.1.2@sha256:1c8edea29d619b169c045360e2e874836b5f65628fad84d43a4eb8c320c13556
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
