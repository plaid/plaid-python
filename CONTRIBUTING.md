# Contributing

## Setup

1. From the `plaid-python` directory, create the `.env` file, which will be used to configure the Plaid client.

  ```
  cp .env.example .env
  ```

2. Go to the [Plaid Dashboard](https://dashboard.plaid.com/) and copy and paste your `client_id`, and `secret` into `.env` using a text editor of your choice. Your account must be enabled for sandbox access.

3. Install the necessary dependencies.

  ```
  make setup
  ```

## Running Tests

Please lint (with `flake8`) and test your pull requests:

```console
$ make lint
$ ./.env make test
```

## Updating Documentation

The generated HTML documentation is served directly from the `master` branch
of the repository. To update the generated documentation:

```console
$ make docs
```
