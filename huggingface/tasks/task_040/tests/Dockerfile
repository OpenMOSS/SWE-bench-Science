ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-040:v0.1.1@sha256:65832254b48e4b1777a7d1d07680a2a870de87c697b47ff8d0c27a516f95ad46
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
