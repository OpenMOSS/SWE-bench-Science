ARG VERIFIER_IMAGE=docker.io/kevinxulearning/swe-bench-science-verifier-matlab-octave-task-025:v0.1.1@sha256:8da94067fe1009753dc73eaf8410b8fe743212c8c1929cc43cb450d3292aac01
FROM ${VERIFIER_IMAGE}

COPY grader.py /tests/grader.py
RUN chmod 755 /tests/grader.py
