.DEFAULT_GOAL := build

base_python := python3
py := poetry run
python := $(py) python

.PHONY: isort
isort:
	$(py) isort -rc aiogram tests

.PHONY: black
black:
	$(py) black aiogram tests

.PHONY: generate
generate:
	$(python) -m generator

build: generate isort black
