install:


run:


debug:


clean: run
	rm -rf */_pycache_ .mypy_cache
	rm -rf .mypy_cache

lint:
	flake8 && mypy . --warn-return-any --warn-unused-ignores --ignore-mising-import --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 && mypy . --strict
