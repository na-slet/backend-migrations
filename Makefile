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

logs:
	docker compose logs

postgres:
	docker compose up -d postgresql

down:
	docker compose down

open_postgres:
	PGPASSWORD=${DB_PASSWORD} docker exec -it parking-map-backend-postgresql psql -U ${DB_USERNAME} -d ${DB_NAME}
