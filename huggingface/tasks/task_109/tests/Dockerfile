ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-109:v0.1.2@sha256:8e53e9700a9b4b5fb91f06bf3a2b9491831173c193787237e6ae1bfd4b9b4892
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
