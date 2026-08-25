ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-094:v0.1.2@sha256:28fafa2333e0604c34c46193fc8f3d8e22b854e24fdba7285c8e8f655b7b01dc
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
