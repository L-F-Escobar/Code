REPORTS 	= tests/reports/
TEST_PATH 	= tests/

.PHONY: help circleci xml html clean clean-pyc clean-reports get-cov-report test clean-egg

.DEFAULT: help

help:
	@echo "Please use \`make <target>' where <target> is one of"
	@echo "  clean      	to remove all pytest cache & coverage report relics"
	@echo "  html       	to make HTML coverage report (index.js)"
	@echo "  xml        	to make XML coverage report"
	@echo "  clean-pyc  	to remove pytest cache relics"
	@echo "  clean-reports  to remove pytest coverage reports"
	@echo "  get-cov-report to check code coverage for cds.Models"
	@echo "  circleci 		to execute on cicd pipline"
	@echo "  test 			to run pytest & coverage"
	@echo "  clean-egg 		removes folders from setup"

install:
	@pip install -r requirements.txt 

circleci:
	@make install

clean-pyc:
	@find . -type d -name __pycache__ -exec rm -r {} \+ \
	&& find . -type d -name .pytest_cache -exec rm -r {} \+ \
	&& find . -type d -name '*.pyc' -exec rm -r {} \+ \
	&& find . -type d -name '*.pyo' -exec rm -r {} \+

clean-egg:
	@rm -rf ./build/ \
	&& rm -rf ./dist/

clean-reports:
	@rm -rf $(REPORTS)

clean:
	@make clean-pyc \
	&& make clean-reports

get-cov-report:
	@coverage report -m models/*

xml:
	@coverage xml

html:
	@coverage html

full-test:
	@coverage run -m pytest -v -s --tb=line $(TEST_PATH) \
	&& make get-cov-report \
	&& make html \
	&& make xml

tests:
	@pytest -v -s --tb=short $(TEST_PATH); \
