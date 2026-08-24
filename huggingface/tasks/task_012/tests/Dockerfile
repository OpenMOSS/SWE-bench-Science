ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-012:v0.1.2@sha256:71e687d9ab5bb57d516d8c59ad7ecaf66dce8295aa7922f32cab601b01ead49b
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
