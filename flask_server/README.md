
# Development model
[![linting: pylint](https://img.shields.io/badge/linting-pylint-yellowgreen)](https://github.com/pylint-dev/pylint)

## Requirements

- `pipx` installed - https://github.com/pypa/pipx
- `poetry` installed (using `pipx`) - https://python-poetry.org/docs/#installing-with-pipx

## Setup

Set up the environment

`poetry install --no-root`

## Quality gates

Typed hints

- Without poetry: `mypy .`
- With poetry: `poetry run mypy .`

## Run the app

Run the server

`poetry run python app.py`