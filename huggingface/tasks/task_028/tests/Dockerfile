ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-028:v0.1.2@sha256:ca8ca8255724890c29c934c7f6b5a6fc24f946c324dde9e3f0a64138e40d73e7
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
