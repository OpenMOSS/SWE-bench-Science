ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-076:v0.1.2@sha256:906a65f8d2c8b7b04d62873482c84217b3f33c4e45e6d77136e2d09d5d08837d
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
