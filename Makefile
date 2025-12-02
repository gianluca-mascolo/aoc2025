.DEFAULT_GOAL := fmt

.PHONY: fmt
fmt:
	poetry run isort .
	poetry run black .
	poetry run flake8 .
