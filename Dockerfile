FROM python:alpine3.7

WORKDIR /app

ADD ./requirements.txt /app/requirements.txt
RUN pip install tox
RUN pip install -r /app/requirements.txt

COPY . /app
