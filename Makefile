.PHONY: all test lint format build clean

test:
	poetry run python -m pytest tests

test_cov:
	poetry run python -m pytest --cov=pysafe_config tests

format:
	# Format tests first
	poetry run python -m isort tests
	poetry run python -m black tests
	# The the package itself
	poetry run python -m isort pysafe_config
	poetry run python -m black pysafe_config

lint:
	poetry run mypy pysafe_config/

	# Check package
	poetry run isort --check-only --diff pysafe_config
	poetry run black --check --diff pysafe_config

	# Check tests
	poetry run isort --check-only --diff tests
	poetry run black --check --diff tests

clean:
	rm -rf .pytest_cache
	rm -f .coverage
	rm -rf .mypy_cache
	rm -f coverage.xml
	rm -rf htmlcov