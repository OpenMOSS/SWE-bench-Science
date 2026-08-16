ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-092:v0.1.1@sha256:c2f3487455d2635edf02c1287cdd318c0679ea22f478d6a871150d5a5447f948
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
