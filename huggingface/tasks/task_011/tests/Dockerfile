ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-011:v0.1.0@sha256:f368455b68e9aa7a13bb1961d2f9a93325626bce0e3ea1f7218b82401dff5568
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
