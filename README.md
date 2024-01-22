# Pre-requisites

- Docker installed
- `pipx` installed - https://github.com/pypa/pipx
- `poetry` installed (using `pipx`) - https://python-poetry.org/docs/#installing-with-pipx

# Docker

Builds the service

`docker-compose build experiment`

Starts the service

`docker-compose up -d`

Run a command within a running container

`docker-compose exec experiment python experiment.py`


# Content

- `/flask_server` - # Proof of concept
