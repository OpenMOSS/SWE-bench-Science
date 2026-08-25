ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-084:v0.1.2@sha256:a836ac7f9cd83faa59982192072ec1ae7a3efeecdc8c45384b73650c3fdcada9
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
