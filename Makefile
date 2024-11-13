start:
	python manage.py runserver

migrate:
	python manage.py migrate

shell:
	python manage.py shell

test:
	python manage.py test 

static:
	python manage.py collectstatic

superuser:
	python manage.py createsuperuser