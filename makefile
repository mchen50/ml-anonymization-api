SHELL := /bin/bash

.ONESHELL:

setup: clean install

activate-venv:
	PIPENV_VENV_IN_PROJECT=1 pipenv shell

install:
	pipenv install --dev

# Run API with pipenv
serve-local:
	pipenv run uvicorn app.main:app --reload

# Run API with Docker
compose-up:
	docker compose up -d --no-deps --build

compose-down:
	docker compose down

test:
	pipenv run pytest tests/

clean-all: clean
	pipenv --rm 

clean:
	rm -rf .coverage; \
	rm -rf .pytest_cache; \
	rm -rf tests/.pytest_cache; \
	find . -type f -name '*.py[co]' -delete -o -type d -name __pycache__ -delete

# Update dependencies and regenerate Pipfile.lock
update:
	pipenv update

# List the installed packages in the virtual environment
list:
	pipenv graph

# Display the path to the virtual environment
venv:
	pipenv --venv

gen-requirements:
	pipenv requirements > requirements.txt

check-format:
	pipenv run black --check --diff .

format:
	pipenv run black .