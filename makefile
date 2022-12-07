venv: 
	python3 -m venv .venv

install: 
	source .venv/bin/activate
	pip install -r requirements.txt