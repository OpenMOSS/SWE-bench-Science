ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-064:v0.1.2@sha256:75f691bdc83ee8de08e902c02b373a99e08b6154db538682d5f8e6ec8690ec25
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
