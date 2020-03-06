FROM python:alpine3.7
RUN apk add --update-cache build-base

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt
RUN pip install tox
RUN pip install -r /app/requirements.txt

COPY . /app
