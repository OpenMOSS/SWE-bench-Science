ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-fortran-task-085:v0.1.2@sha256:2b5ba7ef4e9b60e7b5c9936c1b295c20678ef49e42349d6e8b4412f29d82d1c3
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
