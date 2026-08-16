ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-089:v0.1.0@sha256:66ee7d7df906e3cad4e9d27664f1c6ea9bd6673ef36d5ddd61f5aaa75c88db60
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
