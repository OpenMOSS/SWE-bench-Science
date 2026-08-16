ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-118:v0.1.1@sha256:d9d994d83ed59efa74d512e9306ed84d990a37a00d7ce444e2b6738b124914fd
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
