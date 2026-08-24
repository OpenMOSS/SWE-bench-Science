ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-023:v0.1.2@sha256:18a396490f4a3b79796d8e12d38f29e47a453a67e53c0427d8cdf4a38b33876e
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
