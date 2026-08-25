ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-077:v0.1.2@sha256:56e993f233a4c6f49dee57c5c0f45ee315e4b707cf0761f6d0b36abd010f425f
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
