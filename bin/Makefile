.PHONY: format lint

lint:
	ruff check ./alg-calc
	pyright ./alg-calc
	mypy --check-untyped-defs ./alg-calc
	pylint ./alg-calc

format:
	isort ./alg-calc
	black ./alg-calc

