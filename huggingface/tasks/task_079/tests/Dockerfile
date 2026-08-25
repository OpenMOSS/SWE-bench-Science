ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-079:v0.1.2@sha256:f426f76dedf593220abfb96171146c9791640cc1d290202f211ba5b8834ccdd9
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
