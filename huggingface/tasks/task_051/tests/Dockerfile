ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-fortran-task-051:v0.1.0@sha256:cc4ffda89baf3ef1fed6903ff06b194b1ef2f992413574aa6032451e09e653fb
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
