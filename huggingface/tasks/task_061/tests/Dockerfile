ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-c-task-061:v0.1.1@sha256:e9b9718e2ae8dd4a138053ebd99716be920d0268f2e4b7c034b85bb51e80851c
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
