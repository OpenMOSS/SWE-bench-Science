ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-c-python-task-063:v0.1.2@sha256:93e9e200f3430edcaeaeedce2f1f9593d8b7f9a414002cce4514b3d322467f66
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
