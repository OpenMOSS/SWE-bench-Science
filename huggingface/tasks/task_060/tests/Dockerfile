ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-060:v0.1.2@sha256:ab274b2ce5038b64cf4dc6599183fcc539a143b8f976241ea61ca9307a7f215b
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
