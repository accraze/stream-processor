FROM python:3.7.2-alpine3.9

RUN mkdir /app
WORKDIR /app

RUN pip install pipenv

COPY Pipfile Pipfile
COPY Pipfile.lock Pipfile.lock

RUN pipenv install --deploy --system

COPY src src

ENTRYPOINT celery -A src worker --loglevel=info
