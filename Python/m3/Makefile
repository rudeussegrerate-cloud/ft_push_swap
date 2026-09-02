name = Fly_in


.PHONY: install clean clean-all lint run

install:
	@echo "🚀 Starting fly-in installation..."
	@if [ ! -d "./.venv" ]; then \
		echo "Creating virtual environment..."; \
		python3 -m venv .venv; \
	fi
	@if ! command -v uv >/dev/null 2>&1; then \
		echo "Installing uv..."; \
		curl -LsSf https://astral.sh/uv/install.sh | sh; \
	fi
	@# Explicitly set PATH for this shell session to include uv
	@export PATH="$$HOME/.local/bin:$$PATH"; \
	if ! command -v uv >/dev/null 2>&1; then \
		echo "Error: uv not found after installation. Please restart your shell."; \
		exit 1; \
	fi; \
	echo "Ensuring Python 3.11 is available..."; \
	uv python install 3.11; \
	uv venv --python 3.11; \
	echo "✅ Installation complete. Activate with: source .venv/bin/activate"   


run:
	uv run python3 parser_poo.py

clean:
	@echo "🧹 Cleaning project..."
	@rm -rf \
		__pycache__ \
		.mypy_cache \
		*.egg-info \
		.pytest_cache \
		.python-version \
	@find . -type d -name __pycache__ -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name .vscode -exec rm -rf {} + 2>/dev/null || true
	@find . -type d -name .mypy_cache -exec rm -rf {} + 2>/dev/null || true
	@find . -type f -name "*.pyc" -delete 2>/dev/null || true
	@echo "✅ Clean complete."


clean-all:
	@echo "🧹 Cleaning project and virtual environment..."
	@rm -rf \
		.venv \
		__pycache__ \
		.mypy_cache \
		*.egg-info \
		.pytest_cache \
		.python-version \
	@echo "✅ Full clean complete."

## lint: Run linters and type checker
lint:
	uv run flake8 parser_poo.py
	uv run flake8 --select=D parser_poo.py
	uv run flake8 --max-line-length=79 parser_poo.py
	uv run mypy parser_poo.py --warn-return-any \
		--warn-unused-ignores \
		--ignore-missing-imports \
		--disallow-untyped-defs \
		--check-untyped-defs
