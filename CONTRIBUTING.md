# Contributing

## Setup

1. From the `plaid-python` directory, create the `.env` file, which will be used to configure the Plaid client.

```
cp .env.example .env
```

2. Go to the [Plaid Dashboard](https://dashboard.plaid.com/team/keys) and copy and paste your `client_id`, `public_key`, and Sandbox `secret` into `.env` using a text editor of your choice.

## Requirements

Docker is required to run tests and lint code. Make sure `docker` is available from your command line

## Running Tests

```console
$ make test
```

## Linting

Linting is run automatically when tests are run, but you can also run

```console
$ make lint
```

## Updating Documentation

The generated HTML documentation is served directly from the `master` branch
of the repository. To update the generated documentation:

```console
$ make docs
```
