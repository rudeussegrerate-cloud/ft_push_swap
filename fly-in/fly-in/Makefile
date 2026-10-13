install:
	@command -v uv >/dev/null 2>&1 || (curl -LsSf https://astral.sh/uv/install.sh | sh)
	@if [ ! -f pyproject.toml ]; then \
		~/.local/bin/uv init --bare; \
	fi
	@ ~/.local/bin/uv add -r requirements.txt
	@ ~/.local/bin/uv sync

run:
	@ uv run python3 main.py

debug:
	@ uv run python -m pdb main.py

clean:
	@ find . -type d \( -name "__pycache__" -o -name ".mypy_cache" \) -exec rm -rf {} +

lint:
	@ uv run flake8 . --exclude=.venv/ && uv run mypy . --warn-return-any \
--warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs

lint-strict:
	@ uv run flake8 . --exclude=.venv/ && uv run mypy . --strict

.PHONY: install run debug clean lint lint-strict
