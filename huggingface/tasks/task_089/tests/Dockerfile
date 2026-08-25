ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-089:v0.1.2@sha256:c88f2eb67381db3eb69a9cab98f3280dfe8ec2a08100e0fcd351cd894385b636
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
