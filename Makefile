export FLASK_DEBUG=1
export FLASK_ENV=local
export FLASK_APP=app/__init__.py

clean:
	find app -iname '*.pyc' -exec rm {} \;
	find config -iname '*.pyc' -exec rm {} \;

setup:
	pip install -r requirements.txt
	pip install -r requirements.local.txt

run: clean
	flask run

test:
	FLASK_ENV=test python -m unittest discover -s app/tests -p "test_*.py"

lint:
	flake8 --statistics app

quality: test lint
