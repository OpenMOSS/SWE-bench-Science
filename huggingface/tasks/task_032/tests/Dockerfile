ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-032:v0.1.1@sha256:c75faed022ffcf7321fcfc415227da35e38287acd1304c3cdf6fa487f6b8c2dd
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
