ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-010:v0.1.2@sha256:da78183bad966c8df21b1501d92972394cf4220fb852d89a7b523b246c92f3f0
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
