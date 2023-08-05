# Anonymization API
Streamline the process of building and deploying an inference API on AWS using FastAPI, Docker and Github actions.
API loads spacy NLP model to anonymize information given user input.


## Local Development Notes

Pre-requisites:
```
pyenv<python, pip>, make, pipenv, docker, docker-compose
```

To setup:
```
make activate-venv
make setup
```

To serve the API using pipenv:
```
make serve-local
```

To run the API in docker:
```
make compose-up
```