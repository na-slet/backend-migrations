FROM python:3.10-alpine
WORKDIR /code
RUN apk add --no-cache make
RUN apk add --no-cache poetry
COPY ./Makefile ./Makefile
COPY poetry.lock pyproject.toml ./
RUN make prepare
COPY ./database ./database
COPY ./.env ./.env
CMD make migrate