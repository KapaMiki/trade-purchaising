start:
	pip3 install -r requirements.txt
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver 0.0.0.0:8000
clean:
	find . -type f -name "*.py[co]" -delete
	find . -type d -name "__pycache__" -delete
	find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
	find . -path "*/migrations/*.pyc"  -delete
requirements:
	poetry export --without-hashes -f requirements.txt > requirements.txt
