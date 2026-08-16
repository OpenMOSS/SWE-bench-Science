ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-007:v0.1.0@sha256:ba9b6eeba1b6ac397d7878bff2d920b1137caf4fda6909422fa9001aab26b24b
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
