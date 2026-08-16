ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-094:v0.1.1@sha256:f871bca783e8671572e5c2a95c5e9ce74a5cefdf0fa99298f0514beb63ad5f91
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
