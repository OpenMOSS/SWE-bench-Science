ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-cpp-task-105:v0.1.1@sha256:4e96032a9972da65b1146cc41f8332bda8b16276b7ebf50db8287d5d7a434a96
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
