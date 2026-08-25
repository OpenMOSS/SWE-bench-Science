ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-108:v0.1.2@sha256:e0805a195f550797b5e39a3f9ce26866c331513cf89d30e1cb96a9a5960dacc8
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
