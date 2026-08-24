ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-fortran-task-085:v0.1.1@sha256:57de442f9e3510938ba8203803884f9c824a7d1f1eeee571783fdfa1431dbf56
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
