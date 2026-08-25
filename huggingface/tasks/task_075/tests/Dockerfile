ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-c-task-075:v0.1.2@sha256:7bddaae04159171d9f21bc30355b7cca4393052a536ffc2887c6a017b5e2cb4e
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
