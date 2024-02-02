# Time Series Experiments

## Pre-requisites

- Docker installed

## Docker

Builds the service

`docker-compose build experiment`

Starts the service

`docker-compose up -d`

Run a command within a running container

`docker-compose exec experiment python experiment.py`

## Content

- `/flask_server` - # Proof of concept

## References

- [Blazing fast python docker with poetry](https://medium.com/@albertazzir/blazing-fast-python-docker-builds-with-poetry-a78a66f5aed0)
