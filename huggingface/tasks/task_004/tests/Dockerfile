ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-c-task-004:v0.1.2@sha256:1714f845a65d035a8d39413224fe569efedb98b717dd21eff035222e9348a1a0
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
