[![PyPI version](https://badge.fury.io/py/polygon-api-client.svg)](https://badge.fury.io/py/polygon-api-client)
[![Docs](https://readthedocs.org/projects/polygon-api-client/badge/?version=latest)](https://polygon-api-client.readthedocs.io/en/latest/)

# Polygon Python Client - WebSocket & RESTful APIs

Python client for the [Polygon.io API](https://polygon.io).

## Install

`pip install polygon-api-client`

Requires Python >= 3.8.

## Getting started
See the [Getting Started](https://polygon-api-client.readthedocs.io/en/latest/Getting-Started.html)
section in our docs or view the [examples](./examples) directory.

## Release planning
This client will attempt to follow the release cadence of our API.
When endpoints are deprecated and newer versions are added, the client will
maintain two methods in a backwards compatible way
(e.g. `list_trades` and `list_trades_v4(...)`).
When deprecated endpoints are removed from the API, we'll rename the versioned
method (e.g. `list_trades_v4(...)` -> `list_trades(...)`), remove the old method,
and release a new major version of the client.

The goal is to give users ample time to upgrade to newer versions of our API
_before_ we bump the major version of the client, and in general, we'll try to
bundle breaking changes like this to avoid frequent major version bumps.

Exceptions to this are:

- Methods under `client.vx`. These are expiremental.
- Methods that start with `_*`. We use these internally.
- Type annotations. We may modify these based on our JSON responses.
- We may add model fields.
