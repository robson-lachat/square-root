.PHONY: install test lint format check

install:
	poetry install

test:
	poetry run pytest --cov=src --cov-report=term-missing

lint:
	poetry run ruff check .

format:
	poetry run ruff format .

check: format lint test
