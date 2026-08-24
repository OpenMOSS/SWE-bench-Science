ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-084:v0.1.1@sha256:e22e29a19f68d6cca283927bb26da82063156e070f86f32df8b06bfac15aa3f9
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
