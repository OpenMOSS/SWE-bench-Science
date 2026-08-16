ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-049:v0.1.1@sha256:ba7d3a2168c254fda002f5263c1e7d965577633f0473184e212743416a1d77fb
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
