ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-102:v0.1.1@sha256:adaf1de19b5892112a68f14183079fe298592287c6744d336bcc08997b95b336
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
