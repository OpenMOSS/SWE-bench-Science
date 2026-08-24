ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-090:v0.1.1@sha256:3219d6de7809aaa4ea68f82d5f4ac1bceae44d2480a9ae20f47db039661ad8d6
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
