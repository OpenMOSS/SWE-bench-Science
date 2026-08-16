ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-matlab-octave-task-015:v0.1.1@sha256:1715bcb15924adee88f48c6c62ef62753f5a033f55f198dbbb9fcf83018661e8
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
