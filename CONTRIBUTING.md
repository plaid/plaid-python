# Contributing

Instructions for contributing to [plaid-python][1]. A python client library for the [Plaid API][2]. This library is fully generated from the [Plaid OpenAPI spec][3].

## Setup

1. Run `make pull-openapi`.
2. Install [Docker](https://docs.docker.com/desktop/) if you do not have it on your machine, this helps to isolate any dependency issues.
3. Run `make build-openapi` after you have finished your Docker setup. This generates all the code necessary to run the library.

If you find an issue, please investigate whether it is a type problem with [OpenAPI](3) or a problem with the [python](https://github.com/OpenAPITools/openapi-generator/blob/master/docs/generators/python.md) generator. Then open an issue and Plaid will investigate further.

## Running Tests

1. To build the docker image for the client tests, run `docker build -t plaid-python .`.
2. Go to the [Plaid Dashboard](https://dashboard.plaid.com/) and copy and paste your `client_id` and sandbox `secret` into the following command.
3. Run `docker run --rm -e CLIENT_ID=$CLIENT_ID -e SECRET=$SECRET plaid-python`.

If you wish to run a single test, edit the `tox.ini` file and rebuild the docker image using the command from step 1.

[1]: https://github.com/plaid/plaid-python
[2]: https://plaid.com
[3]: https://github.com/plaid/plaid-openapi
