ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-011:v0.1.2@sha256:db224a611187155658b2ca1a948f594af3c408907f8820e5d27264e11887f1b6
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
