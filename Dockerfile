FROM python:slim

ENV LANG=C.UTF-8 LC_ALL=C.UTF-8 PYTHONUNBUFFERED=1

RUN \
    groupadd celery && \
    useradd -r -g celery celery

COPY --chown=celery:celery . /app
WORKDIR /app

RUN pip install --no-cache-dir celery flower

USER celery
