ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-098:v0.1.2@sha256:18e21b4d6d1a525e2e76eb829ed4a0d01f69004b819ed8746cfed8d428bbf1dc
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
