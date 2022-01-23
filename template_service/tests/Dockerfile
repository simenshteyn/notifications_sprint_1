FROM python:3.10.0-slim-buster

RUN apt-get update && apt-get install -y build-essential libpq-dev \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir /app

WORKDIR /app
ENV PYTHONPATH=${PYTHONPATH}:${PWD}

RUN pip install --upgrade pip && pip --no-cache-dir install poetry

COPY pyproject.toml poetry.lock ./

RUN poetry config virtualenvs.create false

RUN poetry install

RUN mkdir /app/src

COPY src /app/src

RUN mkdir /app/tests

COPY tests /app/tests