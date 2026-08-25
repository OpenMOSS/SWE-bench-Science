ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-104:v0.1.2@sha256:51cda52cad0fd9d866aa74b5b105766a6ebe0dc8a43ff15a99f60be8b4f9420f
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
