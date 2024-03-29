include .env
export

ALEMBIC = database

migrate:
	cd ${ALEMBIC} && poetry run alembic upgrade head

revision:
	cd ${ALEMBIC} && poetry run alembic revision --autogenerate

upgrade:
	cd ${ALEMBIC} && poetry run alembic upgrade +1

downgrade:
	cd ${ALEMBIC} && poetry run alembic downgrade -1

shell:
	poetry shell

prepare:
	poetry install || true

logs:
	docker-compose logs

postgresql:
	docker-compose up -d postgresql

migrator:
	docker-compose up migrator

down:
	docker-compose down || true

rebuild:
	docker-compose build --no-cache

build:
	docker-compose build

open_postgresql:
	PGPASSWORD=${DB_PASSWORD} docker exec -it na-slet-postgresql psql -h localhost -U ${DB_USERNAME} -d ${DB_NAME}
