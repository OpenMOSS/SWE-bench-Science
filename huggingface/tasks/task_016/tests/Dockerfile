ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-cython-task-016:v0.1.2@sha256:5fbf4b76fd2c85e64b655ed6dd5db84814cd1827be058838de569da93e9f9680
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
