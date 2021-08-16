# Contributing

Instructions for contributing to [plaid-python][1]. A python client library for the [Plaid API][2]. This library is fully generated from the [Plaid OpenAPI spec](3).

## Setup

Have a valid version of Python3 installed, as well as docker.

## Running Tests

1. To build the docker image for the client tests, run `docker build -t plaid-python .`.
2. Go to the [Plaid Dashboard](https://dashboard.plaid.com/) and copy and paste your `client_id` and sandbox `secret` into the following command.
3. Run `docker run --rm -e CLIENT_ID=$CLIENT_ID -e SECRET=$SECRET plaid-python`.

If you wish to run a single test, edit the `tox.ini` file and rebuild the docker image using the command from step 1.

[1]: https://github.com/plaid/plaid-python
[2]: https://plaid.com
[3]: https://github.com/plaid/plaid-openapi
