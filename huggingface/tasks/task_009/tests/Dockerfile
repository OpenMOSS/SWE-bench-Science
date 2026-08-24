ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-009:v0.1.2@sha256:fe483ea0e64c344cc2cce2bd520aadc241558e7a7d2f6f397e18267d5bcbf7bb
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
