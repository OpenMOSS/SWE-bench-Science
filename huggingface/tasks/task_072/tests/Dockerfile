ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-072:v0.1.0@sha256:8683aa3c574011f36df457c54a443457cd37078c2ca48f85fcb46015c431b31d
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
