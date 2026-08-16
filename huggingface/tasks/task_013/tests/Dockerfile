ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-013:v0.1.0@sha256:0313891e0ae671a89ca41299c724c36c0331f4b6ebec83979b2e0840a8564717
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
