ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-095:v0.1.2@sha256:e30cb5f6d4f00d9978564085cbd936897bdc9bf3dfedcea280d51a7700c3369c
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
