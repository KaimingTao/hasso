init:
	python3 -m venv env
	@echo "env" >> .gitignore
	./env/bin/pip3 install -r requirements.txt

freeze:
	@./env/bin/pip3 freeze > requirements.txt

build:
	./env/bin/python -m pip freeze > requirements.txt
	./env/bin/python -m pip install --upgrade build
	./env/bin/python -m build

release:
	./env/bin/python -m pip install --upgrade twine
	./env/bin/python -m twine upload dist/* --verbose

test:
	./env/bin/pip install -e .

untest:
	./env/bin/pip uninstall hasso

.PHONY:
	init freeze build release test untest
