ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-087:v0.1.0@sha256:b1ce39c75913bccef5f09acfd2b989857c071fc64c7fdc0dbff092e14dc5270f
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
