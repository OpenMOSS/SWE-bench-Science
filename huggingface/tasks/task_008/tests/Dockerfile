ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-008:v0.1.2@sha256:ea6714179a39cad4d647e9e2a6edf65a0276398d26a12424354ff0009d87f5e7
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
