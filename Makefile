DEV_SETTINGS=development.ini
PROD_SETTINGS=production.ini

help:
	@echo "    clean-pyc"
	@echo "        Remove python artifacts."
	@echo ""
	@echo "    clean-build"
	@echo "        Remove build artifacts."
	@echo ""
	@echo "    install-req"
	@echo "        Install project requirements."
	@echo ""
	@echo "    install-req-test"
	@echo "        Install project test requirements."
	@echo ""
	@echo "    test"
	@echo "        Run py.test"
	@echo ""
	@echo "    init-prod"
	@echo "        Initialize project with production settings."
	@echo ""
	@echo "    init-dev"
	@echo "        Initialize project with development settings."
	@echo ""
	@echo "    run-dev"
	@echo "        Run project with development settings."
	@echo ""
	@echo "    run-prod"
	@echo "        Run project with production settings."
	@echo ""

clean-pyc:
	find . -name \*.pyc -delete

clean-build:
	rm --force --recursive *.egg-info

install-req:
	pip install -e .

test: clean-pyc
	pytest

install-req-test:
	pip install -e ".[testing]"

init-dev: install-req-test
	initialize_pyramid_hs_db $(DEV_SETTINGS)

init-prod: install-req
	initialize_pyramid_hs_db $(PROD_SETTINGS)

run-dev:
	pserve $(DEV_SETTINGS)

run-prod:
	pserve $(PROD_SETTINGS)
