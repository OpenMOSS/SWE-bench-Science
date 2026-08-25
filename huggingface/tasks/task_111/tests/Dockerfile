ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-111:v0.1.2@sha256:992458c03983fd0b7d0e57b244bef9ac4172fef1715d6c5ee63ce0642117fb18
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
