.PHONY: install fmt lint

install:
	poetry install

fmt:
	poetry run black ocha
	poetry run isort ocha

lint:
	poetry run pflake8 ocha
