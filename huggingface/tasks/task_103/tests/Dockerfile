ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-103:v0.1.2@sha256:6d93306bc556b07316758e0676c400bb9d12917b186af931b6d3c0a5db647aff
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
