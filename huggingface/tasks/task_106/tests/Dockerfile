ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-106:v0.1.2@sha256:2fd09d210c6eac904dc98ea9055a8d74ca08076c9321455bc10cd99b7abfdfec
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
