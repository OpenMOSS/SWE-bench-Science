ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-118:v0.1.2@sha256:9adaec411be66f4196e22bcf44c8cd9c3d0f4090a7623ab931a064856e74a83b
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
