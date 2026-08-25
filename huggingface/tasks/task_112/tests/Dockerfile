ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-112:v0.1.2@sha256:bdaf5e5af8ea7093be2e4b0c12239125e43569a0f8ce16642656ec81ecc2ccd6
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
