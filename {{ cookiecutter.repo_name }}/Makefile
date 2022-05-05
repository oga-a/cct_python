PROJECT_NAME := {{ cookiecutter.python_package }}
RUN := poetry run

.PHONY: check
check: test lint mypy

.PHONY: install
install:
	@poetry install

.PHONY: test
test: pytest doctest

.PHONY: pytest
pytest:
	$(RUN) pytest --doctest-modules tests

.PHONY: doctest
doctest:
	$(RUN) pytest --doctest-modules $(PROJECT_NAME)

.PHONY: test-cov
test-cov:
	$(RUN) pytest --cov=$(PROJECT_NAME) --cov-report=html

.PHONY: lint
lint: lint-black lint-isort lint-flake8

.PHONY: lint-black
lint-black:
	$(RUN) black --check --diff --quiet --skip-magic-trailing-comma .

.PHONY: lint-isort
lint-isort:
	$(RUN) isort --check --force-single-line-imports --quiet .

.PHONY: lint-flake8
lint-flake8:
	$(RUN) pflake8 --exclude tests

.PHONY: mypy
mypy:
	$(RUN) mypy $(PROJECT_NAME)

.PHONY: format
format: format-black format-isort

.PHONY: format-black
format-black:
	$(RUN) black --quiet --skip-magic-trailing-comma .

.PHONY: format-isort
format-isort:
	$(RUN) isort --force-single-line-imports --quiet .

# TODO: format-flake8追加

# sphinx-apidocは追記したが、必要なかった？
.PHONY: doc
doc:
	sphinx-apidoc -e -f -o ./docs/source .
	rm ./docs/source/modules.rst
	rm ./docs/source/tests*.rst
	@cd docs && make html

# .PHONY: publish
# publish:
# 	@git checkout master
# 	@gh repo sync {{ cookiecutter.github_username }}/$(PROJECT_NAME)
# 	@gh workflow run publish.yml --repo {{ cookiecutter.github_username }}$(PROJECT_NAME)

.PHONY: jn
jn:
	$(RUN) jupyter notebook

.PHONY: jl
jl:
	$(RUN) jupyter lab

# TODO: markdownlint
