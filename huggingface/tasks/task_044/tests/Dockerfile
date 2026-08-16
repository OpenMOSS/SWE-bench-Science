ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-044:v0.1.1@sha256:71ce7ba80a7fa8e30f073a714ed124130925d8fc6945760d3b28e176bdba2973
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
