ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-029:v0.1.0@sha256:bf60c02145e60447a42aa0e8205c11851bafae01fb38da1969c8ca9697ab119f
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
