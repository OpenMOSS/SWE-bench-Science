ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-083:v0.1.2@sha256:e147977aebc6fa8a2f11683ae001f26725041860bfaf76189b610285840106d4
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
