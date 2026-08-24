ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-007:v0.1.2@sha256:917114c3ffdb183152bb669276dd99ef7838e7530cbeee0b03f2e33bbe4e949b
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
