ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-078:v0.1.2@sha256:3f948b28a949977948127b02bc9e7649eaad739aa5df6b74654f9da70d0fda87
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
