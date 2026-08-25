ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-099:v0.1.2@sha256:87d4b9026e4ed7bcd46565d4cbe7c418c181f03f2e7d8fa8a4abbbdeb22c53a8
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
