ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-057:v0.1.1@sha256:1d75dca821fc4db5d8aa24f38b393e6c17703c69e1a20ce256a64b908fe7a60f
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
