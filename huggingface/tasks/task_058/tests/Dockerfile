ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-cpp-task-058:v0.1.1@sha256:66508091435ada9bb6766098d309d1a932d610da54a2205db48521b3dc8a4e0d
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
