.DEFAULT_GOAL := help 

.PHONY: help
help:  ## Show this help.
	@grep -E '^\S+:.*?## .*$$' $(firstword $(MAKEFILE_LIST)) | \
		awk 'BEGIN {FS = ":.*?## "}; {printf "%-30s %s\n", $$1, $$2}'

.PHONY: init
init: ## init venv
	. .venv/bin/activate

.PHONY: run
run: ## Runs main program
	uv run fizzbuzz/fizzbuzz.py

.PHONY: test
test: ## run tests
	pytest -v --cov tests
