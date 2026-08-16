ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-111:v0.1.1@sha256:d1f89ef44d00ba6a6d86fbd9c38160846d3925cfd06982d4d11f745c2e43d4e6
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
