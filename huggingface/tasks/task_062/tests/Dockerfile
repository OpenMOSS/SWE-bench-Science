ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-062:v0.1.1@sha256:ac14a3bfe33e6c172748db20cb6a552eaafced87dccfcc6a808ab4de598b444e
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
