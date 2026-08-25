ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-107:v0.1.2@sha256:7db7880a15a0ce7332709262897b2eeadf9a19145d9f3eae6cb190c4a16b497b
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
