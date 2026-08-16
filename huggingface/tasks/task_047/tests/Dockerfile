ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-047:v0.1.1@sha256:6255287669b4711882fdd9c817e94e31ba63f6cbc228a2469763f45b3019144b
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
