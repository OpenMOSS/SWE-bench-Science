ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-115:v0.1.2@sha256:fe262769f161b8838afbb762c8ec40caa2e990a6fed9e8125a3789bc24c8754b
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
