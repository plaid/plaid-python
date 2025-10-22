# Note: This image is also built in CircleCI, so limit references to internal repositories.
FROM 345594567237.dkr.ecr.us-east-1.amazonaws.com/docker-hub/library/python:3.7

# Create app directory
WORKDIR /usr/src/app

# Copy app to directory
COPY . /usr/src/app

# newer versions of tox fail on circleci for some reason
# https://discuss.circleci.com/t/python-tox-doesnt-build-anymore/35059
RUN pip install tox==3.15.0
RUN pip install -r requirements.txt

CMD ["make", "test"]
