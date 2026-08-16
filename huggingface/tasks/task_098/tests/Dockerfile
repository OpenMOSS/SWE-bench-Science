ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-098:v0.1.1@sha256:55b18bf0203de35a647f1cb292cf10b6381429a77a9858bd90bf79701a0ada0a
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
