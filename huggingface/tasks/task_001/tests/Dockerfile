ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-001:v0.1.0@sha256:7af68a1c44876615b0f961abd18e7fb656dae5f117820a35ff8e1d10faa430b0
FROM ${VERIFIER_IMAGE}

# Keep the runtime entrypoint in sync with the task bundle. This is also
# mounted by the task compose override when a prebuilt verifier image is used.
COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
