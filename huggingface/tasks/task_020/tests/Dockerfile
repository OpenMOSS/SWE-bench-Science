ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-020:v0.1.2@sha256:aed7b7c497b3fd2eb7b532fb353e730f39e230db4fa3762992aa54deccc54267
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
