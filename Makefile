install:
	uv sync

lint:
	uv run ruff check .

lint-fix:
	uv run ruff check --fix .

test-numbers:
	uv run pytest -v tests/test_numbers.py::TestNumbersFunctions

test-strings:
	uv run pytest -v tests/test_strings.py::TestStringsFunctions

test-boolean:
	uv run pytest -v tests/test_boolean.py::TestBooleanFunctions

test-loops:
	uv run pytest -v tests/test_loops.py::TestLoopsFunctions

test-branching:
	uv run pytest -v tests/test_branching.py::TestBranchingFunctions

test-lists:
	uv run pytest -v tests/test_lists.py::TestListsFunctions

test-sets:
	uv run pytest -v tests/test_sets.py::TestSetsFunctions

test-dicts:
	uv run pytest -v tests/test_dicts.py::TestDictsFunctions

test:
	uv run pytest