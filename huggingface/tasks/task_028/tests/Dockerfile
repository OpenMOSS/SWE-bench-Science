ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-028:v0.1.0@sha256:4c4ec965b94251ab9b163fe1294a4e863dc5a2b0a005dabb51dbaa5a5d6c95fe
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
