build:
	python -m pip install --upgrade build
	python -m build

release:
	python -m pip install --upgrade twine
	python -m twine upload dist/*


.PHONY:
	init dep all build
