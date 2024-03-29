# Dockerfile-experiment

FROM python:3.12-slim-bullseye

RUN pip install poetry==1.7.1

ENV POETRY_NO_INTERACTION=1 \
    POETRY_VIRTUALENVS_IN_PROJECT=1 \
    POETRY_VIRTUALENVS_CREATE=1 \
    POETRY_CACHE_DIR=/tmp/poetry_cache

WORKDIR /app

COPY pyproject.toml poetry.lock ./
RUN touch README.md

RUN poetry install --without dev --no-root && rm -rf $"POETRY_CACHE_DIR"

COPY src .

RUN poetry install --without dev

#ENTRYPOINT ["poetry", "run", "python", "-m", "app"]
ENTRYPOINT ["poetry", "run", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "5000"]
