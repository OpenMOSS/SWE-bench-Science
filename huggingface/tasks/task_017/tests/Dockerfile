ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-017:v0.1.2@sha256:082a831bd6af86c7a13fd06feddd97a9886990571583a42a9f9ec829c2f05873
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
