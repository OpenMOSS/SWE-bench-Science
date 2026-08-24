ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-065:v0.1.2@sha256:a115c7e2c807ecff0281bbda71a6825aafac76c159fae889db9f5a1b20cc3aab
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
