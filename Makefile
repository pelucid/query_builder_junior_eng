venv:
ifndef VIRTUAL_ENV
ifndef CONDA_PREFIX
$(error VIRTUAL / CONDA ENV is not set - please activate environment)
endif
endif

build: venv
	pip install -Ur requirements.txt
	pip install -Ur requirements_private.txt

test: venv
	pytest -svv query_builder/tests/

run: venv
	python query_builder/app/server.py
