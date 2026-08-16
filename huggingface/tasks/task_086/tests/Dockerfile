ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-086:v0.1.0@sha256:fb47312ac7443db59115807334c5d2345e3a2fb7a8f83d89bc8bfb48f7ce4bac
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
