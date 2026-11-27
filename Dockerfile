# Note: This image is also built in CircleCI, so limit references to internal repositories.
### Build stage
FROM python:3.7 AS builder

# Create app directory
WORKDIR /usr/src/app

# Copy app to directory
COPY . /usr/src/app

# newer versions of tox fail on circleci for some reason
# https://discuss.circleci.com/t/python-tox-doesnt-build-anymore/35059
# External CircleCI builds use PyPI. Plaid builds can pass the pipconf secret.
RUN --mount=type=secret,id=pipconf,target=/etc/pip.conf \
    pip install --require-hashes --only-binary=:all: -r requirements-build.txt && \
    pip install --require-hashes --no-build-isolation --only-binary=:all: \
        --no-binary=cov-core,flake8-mutable,coverage -r requirements-docker.txt && \
    pip check

ENV TOXENV=docker VIRTUALENV_NO_PERIODIC_UPDATE=1

### Runtime stage
FROM python:3.7
COPY --from=builder /usr/src/app /usr/src/app
WORKDIR /usr/src/app

CMD ["make", "test"]
