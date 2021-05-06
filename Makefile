ARG := $(word 2, $(MAKECMDGOALS))


startdocker:
	docker-compose up backend

prepare:
	docker-compose up -d pgadmin

compile: checkvenv
	pip-compile --allow-unsafe -o dev-requirements.txt dev-requirements.in
	pip-compile -o requirements.txt requirements.in
	make install

install: checkvenv
	pip-sync requirements.txt dev-requirements.txt

start: checkvenv
	./manage.py runserver

test: checkvenv
	./manage.py test $(ARG) --keepdb

shell: checkvenv
	./manage.py shell_plus

migrate: checkvenv
	./manage.py makemigrations
	./manage.py migrate

setupvenv: checkvenv
	pip install pip-tools
	make install
	pre-commit install
	pre-commit install --hook-type pre-push
	make migrate

checkvenv:
	./tools/check_venv.sh
