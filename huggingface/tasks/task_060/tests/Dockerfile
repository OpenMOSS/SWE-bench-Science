ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-060:v0.1.0@sha256:d1a95a1456b922044d1cfa9156bf33ba40628a3115b2ff25b4d6b149dfd1f4bf
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
