ARG BASE_IMAGE=python:3.11-slim
FROM ${BASE_IMAGE}

ARG INSTALL_FORTRAN=1
ARG INSTALL_OCTAVE=0
ENV DEBIAN_FRONTEND=noninteractive \
    PIP_DISABLE_PIP_VERSION_CHECK=1 \
    PIP_NO_CACHE_DIR=1 \
    PYTHONDONTWRITEBYTECODE=1

RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        build-essential \
        ca-certificates \
        curl \
        git \
        ripgrep \
    && rm -rf /var/lib/apt/lists/*

RUN if [ "${INSTALL_FORTRAN}" = "1" ]; then \
        apt-get update \
        && apt-get install -y --no-install-recommends gfortran \
        && rm -rf /var/lib/apt/lists/*; \
    fi \
    && if [ "${INSTALL_OCTAVE}" = "1" ]; then \
        apt-get update \
        && apt-get install -y --no-install-recommends octave \
        && rm -rf /var/lib/apt/lists/*; \
    fi

WORKDIR /app/task_038
COPY repo/ /app/task_038/source/
COPY public/ /app/task_038/
COPY requirements.lock /app/task_038/requirements.lock

RUN python -m pip install --no-cache-dir --upgrade pip \
    && python -m pip install --no-cache-dir -r requirements.lock
ENV PYTHONPATH=/app/task_038:/app/task_038/source

RUN git init \
    && git checkout -b main \
    && git config user.email science-bench@example.invalid \
    && git config user.name "SWE-bench Science baseline" \
    && git add -A \
    && GIT_AUTHOR_DATE=2025-01-01T00:00:00Z \
       GIT_COMMITTER_DATE=2025-01-01T00:00:00Z \
       git commit -m baseline \
    && git reflog expire --expire=now --all \
    && git gc --prune=now

CMD ["bash"]
