
# Experiment with Python frameworks and timeseries DB

[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

## Requirements

- `pipx` installed - https://github.com/pypa/pipx
- `poetry` installed (using `pipx`) - https://python-poetry.org/docs/#installing-with-pipx

## Setup

Set up the environment

`poetry install --no-root`

## Quality gates

Typed hints (`pyright`)

- Without poetry: `pyright .`
- With poetry: `poetry run pyright .`

Style guide (`pylint`)

- Without poetry: `pylint src/`
- With poetry: `poetry run pylint *py`

## Run the app

Run the server

`poetry run python app.py`