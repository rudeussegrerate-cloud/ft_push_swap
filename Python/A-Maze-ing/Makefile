VENV = venv
PYTHON = $(VENV)/bin/python3
PIP = $(VENV)/bin/pip

install: config.txt
		$(PIP) install -r config.txt

run: $(VENV)/bin/activate
		$(PYTHON) a_maze_ing.py config.txt

debug:
		python3 -m pdb a_maze_ing.py

clean:
		rm -rf __pycache__
		rm -rf $(VENV)

lint:
		flake8 --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs .
		mypy --warn-return-any --warn-unused-ignores --ignore-missing-imports --disallow-untyped-defs --check-untyped-defs .
