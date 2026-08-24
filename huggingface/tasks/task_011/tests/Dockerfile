ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-011:v0.1.0@sha256:a2cce1bf22739b0728b7de005fb8bf8473fd95cc362409fc529a918dd4ca87b7
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
