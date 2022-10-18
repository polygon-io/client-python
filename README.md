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

## Contributing

If you found a bug or have an idea for a new feature, please first discuss it with us by
[submitting a new issue](https://github.com/polygon-io/client-python/issues/new/choose).
We will respond to issues within at most 3 weeks.
We're also open to volunteers if you want to submit a PR for any open issues but
please discuss it with us beforehand. PRs that aren't linked to an existing issue or
discussed with us ahead of time will generally be declined. If you have more general
feedback or want to discuss using this client with other users, feel free to reach out
on our [Slack channel](https://polygon-io.slack.com/archives/C03FRFN7UF3).

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
