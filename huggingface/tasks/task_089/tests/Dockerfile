ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-python-task-089:v0.1.1@sha256:81bdeadb79aef5428d6c184bfe73a9c8612cd35576817b8e3b650bbd25daea9f
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
