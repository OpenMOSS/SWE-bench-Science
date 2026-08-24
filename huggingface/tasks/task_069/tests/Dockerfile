ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-069:v0.1.2@sha256:b553135a9e14baed582cc3eb5f48424c14155246f68b2fe13a905e6759e884b9
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
