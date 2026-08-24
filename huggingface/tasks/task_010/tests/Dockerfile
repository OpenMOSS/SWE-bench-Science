ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-010:v0.1.0@sha256:fe5b09f4a5b92039fc793cd50a3feb28c9828eed93a42e4392fb2ea0d0402d11
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
