ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-001:v0.1.0@sha256:0d884c02831bea451e74ece1d7bce1eab7c799f34a50f4a434d23861dee53b43
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
