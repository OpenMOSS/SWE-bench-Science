ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-080:v0.1.0@sha256:0bd2b80b544ce97b0ecbab0c397a5d68014ee7cb2c3133be648db3d3ca0045ed
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
