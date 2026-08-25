ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-116:v0.1.2@sha256:815e86c855c56edadd6f840d067f93706f013a8c9dbca24bb1c5f5874a2f8baf
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
