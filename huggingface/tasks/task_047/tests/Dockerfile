ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-047:v0.1.2@sha256:993a6cff055e27d925f38f332e6b53882052f6f0edf5b4e09e6b8a3e9b8e1fbb
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
