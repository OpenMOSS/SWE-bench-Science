ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-072:v0.1.2@sha256:701358aa75f00864e880ff11f4323b3e661c1e4ba27f980b995eee61b67422d5
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
