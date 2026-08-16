ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-065:v0.1.1@sha256:7cf23632e18d6c06f29162b88665e2c0e37f37b8c4d7e2d4f911a1394c24a015
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
