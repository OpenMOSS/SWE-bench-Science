ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-052:v0.1.2@sha256:935154738d5dfcd390f938b928169bc13d490188c93ff34894c8e68556a53779
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
