ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-008:v0.1.0@sha256:5f02708ac41337aa21e611a45fc0b398613378833718f2900a18ae753808974a
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
