run:
	python out/bundle.py

build:
	python build.py

setup: requirements.txt
	pip install -r requirements.txt
