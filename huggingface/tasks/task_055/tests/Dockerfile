ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-055:v0.1.1@sha256:3fcc630e3894beeac75efb4a0af160c6d174432a0eccfa2f14432fad8890f97d
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
