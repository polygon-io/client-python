[![PyPI version](https://badge.fury.io/py/polygon-api-client.svg)](https://badge.fury.io/py/polygon-api-client)
[![Docs](https://readthedocs.org/projects/polygon-api-client/badge/?version=latest)](https://polygon-api-client.readthedocs.io/en/latest/)

# Polygon Python Client - WebSocket & RESTful APIs

Python client for the [Polygon.io API](https://polygon.io).

## Install

`pip install polygon-api-client~=1.0.0b`

Requires Python >= 3.8.

## Getting started
See the [Getting Started](https://polygon-api-client.readthedocs.io/en/latest/Getting-Started.html)
section in our docs or view the [examples](./examples) directory.

# Contributing

For now, we're generally not accepting pull requests from outside contributors
but we're open to bug reports and feature requests. Or if you have more general
feedback, feel free to reach out on
our [Slack channel](https://polygon.io/contact).

## Release planning
This client will attempt to follow the release cadence of our API.
When endpoints are deprecated and newer versions are added, the client will
maintain two methods in a backwards compatible way
(e.g. `get_trades` and `get_trades_v4(...)`).
When deprecated endpoints are removed from the API, we'll rename the versioned
method (e.g. `get_trades_v4(...)` -> `get_trades(...)`), remove the old method,
and release a new major version of the client.

The goal is to give users ample time to upgrade to newer versions of our API
_before_ we bump the major version of the client, and in general, we'll try to
bundle breaking changes like this to avoid frequent major version bumps.

One exception to this is our vX API. Methods that fall under `client.vx` are
considered experimental and may be modified or deprecated as needed.
We'll call out any breaking changes to vX endpoints in our release notes to
make using them easier.
