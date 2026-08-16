ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-027:v0.1.1@sha256:7553e8b9d60ddba9b86ee74d4f200929dfaed195b79a7e29efa3713f93e5a656
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
