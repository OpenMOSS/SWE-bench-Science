ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-099:v0.1.1@sha256:117e303dd4687f1a1f5963a72992875c417b925a2ab1c6225f7a7abed0f280bd
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
