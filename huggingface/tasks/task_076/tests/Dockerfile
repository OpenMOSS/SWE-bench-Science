ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-076:v0.1.0@sha256:c40da6ce2cafe0194e2d74ca0380587b696890713c163a17624a855c86247404
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
