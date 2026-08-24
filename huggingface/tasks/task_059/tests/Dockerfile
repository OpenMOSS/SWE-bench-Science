ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-059:v0.1.2@sha256:08f21f455ab40f7f746fe58ea55c82817f774cd6685280463e2851b74c2b10f4
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
