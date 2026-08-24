ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-027:v0.1.2@sha256:f942dae48c37c9a845fe097d7987a4a0d926c7b0cb3d0d8272c30979266d7c63
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
