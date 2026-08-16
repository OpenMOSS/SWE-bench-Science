ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-fortran-task-085:v0.1.0@sha256:e68ac55c7cfb257756103351c305b97789d72f1e79203305d2aa7fa39e657eb1
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
