ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-019:v0.1.0@sha256:ffba9cf85dd9585323f72ac3e160da993c4f9ebb66846aa95071a62346e62330
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
