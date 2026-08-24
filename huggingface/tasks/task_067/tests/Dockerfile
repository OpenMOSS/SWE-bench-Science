ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-067:v0.1.2@sha256:d4b000d7a859cc21663a08f381649f408a27e8376d792d17a7c0c97a458387e0
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
