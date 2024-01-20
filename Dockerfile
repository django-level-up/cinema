FROM python:3.11-slim

LABEL maintainer="github/safarovqodirjon"

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

ARG DEV=false
ARG TEST=false
ARG PROD=false
ARG DEP=false
ENV DEV=$DEV
ENV TEST=$TEST
ENV PROD=$PROD
ENV DEP=$DEP

RUN mkdir cinema/
COPY ./app/ cinema/app/
COPY ./infrastructure/ cinema/infrastructure/
WORKDIR cinema/app/

EXPOSE 800
RUN python3 -m venv /.venv/ && \
    /.venv/bin/pip install --upgrade pip && \
    if [ "$PROD" = "true" ]; then /.venv/bin/pip install -r ../infrastructure/prod/requirements.txt; fi && \
    if [ "$DEV" = "true" ]; then /.venv/bin/pip install -r ../infrastructure/dev/requirements.txt; fi && \
    if [ "$TEST" = "true" ]; then /.venv/bin/pip install -r ../infrastructure/test/requirements.txt; fi && \
    adduser --disabled-password --no-create-home django-user

USER root
RUN chmod -R 777 /cinema
RUN chown -R django-user /cinema

USER django-user

ENV PATH="/.venv/bin/:$PATH"
