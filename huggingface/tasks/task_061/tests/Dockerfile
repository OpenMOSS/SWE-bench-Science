ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-c-task-061:v0.1.2@sha256:02243af35f5670de51ef31798ef554e420143a921b0265aad174230a99f8470c
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
