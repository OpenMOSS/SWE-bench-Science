ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-003:v0.1.0@sha256:4d2e13b726b99a0c9d302ba913cdaa727c49fdc403b65b68918ec70c1713a790
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
