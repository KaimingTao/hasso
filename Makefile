build:
	./env/bin/python -m pip freeze > requirements.txt
	./env/bin/python -m pip install --upgrade build
	./env/bin/python -m build

release:
	./env/bin/python -m pip install --upgrade twine
	./env/bin/python -m twine upload dist/*

.PHONY:
	init dep all build
