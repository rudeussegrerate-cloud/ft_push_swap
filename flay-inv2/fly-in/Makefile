install:
	curl -LsSf https://astral.sh | sh
	uv init --bare
	uv add -r requirements.txt
	uv sync

run:
	uv run main.py

debug:
	uv run python -m pdb main.py --verbose

clean:
	find . -type d \(-name "__pycache__" -o -name ".mypy_cache") exec rm -rf {} +

lint:
	flake8 . && mypy . --warn-return-any --warn-unused-ignores\
	--ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	flake8 . && mypy . --strict

.PHONY: install run debug clean lint lint-strict
