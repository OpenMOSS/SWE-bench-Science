ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-053:v0.1.2@sha256:82a0199bf6414261b926827479853533905a3208a077419adce59a27df7e5a2d
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
