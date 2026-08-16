ARG VERIFIER_IMAGE=science-bench-task-verifier-pending:canary
FROM ${VERIFIER_IMAGE}

# Keep the runtime entrypoint in sync with the task bundle. This is also
# mounted by the task compose override when a prebuilt verifier image is used.
COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
