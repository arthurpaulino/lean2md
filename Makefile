.PHONY: dist upload_test upload_pypi

dist:
	@rm -rf dist && python setup.py sdist

upload_test:
	@python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

upload_pypi:
	@python -m twine upload dist/*
