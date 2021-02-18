
FROM python:3.7

# Create app directory
WORKDIR /usr/src/app

# Copy app to directory
COPY . /usr/src/app

RUN pip install tox==3.15.0
RUN pip install -r requirements.txt

CMD ["make", "test"]

