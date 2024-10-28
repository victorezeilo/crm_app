# Variables
VENV_DIR := crm_venv
PYTHON := $(VENV_DIR)/bin/python
PIP := $(VENV_DIR)/bin/pip
DJANGO_MANAGE := $(PYTHON) manage.py

## Install dependencies and set up virtual environment
setup: $(VENV_DIR) requirements.txt
	$(PIP) install -r requirements.txt

$(VENV_DIR):
	python3 -m venv $(VENV_DIR)

## Run Django server
runserver:
	$(DJANGO_MANAGE) runserver

## Run linting with Flake8
lint:
	$(PYTHON) -m flake8 .

## Run migrations
migrate:
	$(DJANGO_MANAGE) migrate

## Make migrations
makemigrations:
	$(DJANGO_MANAGE) makemigrations

## Clean up unnecessary files
clean:
	find . -name "__pycache__" -exec rm -rf {} +
	find . -name "*.pyc" -exec rm -f {} +

