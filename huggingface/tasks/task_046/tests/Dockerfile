ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-046:v0.1.1@sha256:25d3e2f3e860c3712da3b56d584c4cf8abd297551527e87d8547323f9aa1c9a1
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
