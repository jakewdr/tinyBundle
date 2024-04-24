run:
	make build
	python out/bundle.py -OO

build:
	python tinyBundle.py -OO

setup: requirements.txt
	pip install -r requirements.txt