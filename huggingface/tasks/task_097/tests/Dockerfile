ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-097:v0.1.1@sha256:12cbdb609f7316d4fa2700879bdbaedfb066aa2df6f0a4a5a8686204efa152c2
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
