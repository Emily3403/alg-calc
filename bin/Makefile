.PHONY: format lint

lint:
	ruff check ./alg_calc
	pyright ./alg_calc
	mypy --check-untyped-defs ./alg_calc
	pylint ./alg_calc

format:
	isort ./alg_calc
	black ./alg_calc

