ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-113:v0.1.2@sha256:b19cd02c4ee297fd4fb807c65808ee80685c8ebf8e268cc005cc96fd44683958
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
