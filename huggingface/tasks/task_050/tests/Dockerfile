ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-050:v0.1.1@sha256:329b4cefbac68b9fff040c801b61c9edc46971f6378547731630f50d353d6a48
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
