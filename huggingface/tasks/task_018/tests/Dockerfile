ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-cython-task-018:v0.1.2@sha256:cafed37fe86f1e5427b89529dd87df4a619c3f6585e94e794ec8c91d98bb4dc7
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
