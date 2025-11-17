.PHONY: all test lint format build clean

test:
	poetry run python -m pytest tests

format:
	poetry run python -m isort tests
	poetry run python -m black tests
	poetry run python -m isort pysafe_config
	poetry run python -m black pysafe_config