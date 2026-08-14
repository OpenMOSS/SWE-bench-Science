ARG BASE_IMAGE=python:3.11-slim
FROM ${BASE_IMAGE}

COPY private_tests/ /tests/private_tests/
COPY test.sh /tests/test.sh
COPY grader.py /tests/grader.py
RUN chmod 755 /tests/test.sh /tests/grader.py

CMD ["/tests/test.sh"]
