ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-057:v0.1.2@sha256:48244f6428f8e23b5707b9b48799ebe852f0866b6bb7a136f5033edf95dfed0c
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
