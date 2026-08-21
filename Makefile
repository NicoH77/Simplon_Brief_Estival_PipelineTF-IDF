.PHONY: format lint test benchmark quality

format:
	ruff format .

lint:
	ruff check .

test:
	pytest -q

benchmark:
	python -m src.benchmark

quality: format lint test