TEST_PATH=pyramid_hs/
DEV_SETTINGS=development.ini
PROD_SETTINGS=production.ini

clean-pyc:
	find . -name \*.pyc -delete

clean-build:
	rm --force --recursive *.egg-info

install-req:
	pip install -e .

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

test: clean-pyc
    py.test --verbose --color=yes $(TEST_PATH)
