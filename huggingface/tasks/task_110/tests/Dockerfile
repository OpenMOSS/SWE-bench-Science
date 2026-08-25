ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-110:v0.1.2@sha256:cad750ffb51996985e6c9bd5f9c3eb8ae68022cbf11c7ad4b9c29ff994722c57
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
