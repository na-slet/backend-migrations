include .env
export

ALEMBIC = database

migrate:
	cd ${ALEMBIC} && python3 -m poetry run alembic upgrade head

revision:
	cd ${ALEMBIC} && python3 -m poetry run alembic revision --autogenerate

upgrade:
	cd ${ALEMBIC} && python3 -m poetry run alembic upgrade +1

downgrade:
	cd ${ALEMBIC} && python3 -m poetry run alembic downgrade -1

shell:
	python3 -m poetry shell

prepare:
	python3 -m poetry install | true

logs:
	docker-compose logs

postgres:
	docker-compose up -d postgresql

migrator:
	docker-compose up -d migrator

down:
	docker-compose down

open_postgres:
	PGPASSWORD=${DB_PASSWORD} psql -h ${DB_HOST} -U ${DB_USERNAME} -d ${DB_NAME}
