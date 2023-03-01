[![PyPI version](https://badge.fury.io/py/polygon-api-client.svg)](https://badge.fury.io/py/polygon-api-client)
[![Docs](https://readthedocs.org/projects/polygon-api-client/badge/?version=latest)](https://polygon-api-client.readthedocs.io/en/latest/)

# Polygon Python Client - WebSocket & RESTful APIs

Python client for the [Polygon.io API](https://polygon.io).

## Install

```
pip install polygon-api-client
```
Requires Python >= 3.8.

## Getting started

To get started, please see the [Getting Started](https://polygon-api-client.readthedocs.io/en/latest/Getting-Started.html) section in our docs, view the [examples](./examples) directory for code snippets, or view the [blog post with videos](https://polygon.io/blog/polygon-io-with-python-for-stock-market-data/) to learn more.

## REST API Client
Import the RESTClient.
```python
from polygon import RESTClient
```
Create a new client with your [API key](https://polygon.io/dashboard/api-keys)
```python
client = RESTClient(api_key="<API_KEY>")
```
### Using the Client
Request data using client methods.
```python
ticker = "AAPL"

# List Aggregates (Bars)
bars = client.get_aggs(ticker=ticker, multiplier=1, timespan="day", from_="2023-01-09", to="2023-01-10")
for bar in bars:
    print(bar)

# Get Last Trade
trade = client.get_last_trade(ticker=ticker)
print(trade)

# List Trades
trades = client.list_trades(ticker=ticker, timestamp="2022-01-04")
for trade in trades:
    print(trade)

# Get Last Quote
quote = client.get_last_quote(ticker=ticker)
print(quote)

# List Quotes
quotes = client.list_quotes(ticker=ticker, timestamp="2022-01-04")
for quote in quotes:
    print(quote)
```
Note: For parameter argument examples check out our docs. All required arguments are annotated with red asterisks " * " and argument examples are set.
Check out an example for Aggregates(client.get_aggs) [here](https://polygon.io/docs/stocks/get_v2_aggs_ticker__stocksticker__range__multiplier___timespan___from___to)

## WebSocket Client 

Import classes
```python
from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List
```
### Using the client
Create a new client with your [API key](https://polygon.io/dashboard/api-keys) and subscription options.
```python
# Note: Multiple subscriptions can be added to the array 
# For example, if you want to subscribe to AAPL and META,
# you can do so by adding "T.META" to the subscriptions array. ["T.AAPL", "T.META"]
# If you want to subscribe to all tickers, place an asterisk in place of the symbol. ["T.*"]
ws = WebSocketClient(api_key=<API_KEY>, subscriptions=["T.AAPL"])
```
Create a handler function and run the WebSocket.
```python
def handle_msg(msg: List[WebSocketMessage]):
    for m in msg:
        print(m)

ws.run(handle_msg=handle_msg)
```
Check out more detailed examples [here](https://github.com/polygon-io/client-python/tree/master/examples/websocket).

## Launchpad
Users of the Launchpad product will need to pass in certain headers in order to make API requests using the RequestOptionBuilder.
Example can be found [here](./examples/launchpad).

Import classes
```python
from polygon import RESTClient
from polygon.rest.models.request import RequestOptionBuilder
```
### Using the client
Create client and set options
```python
# create client
c = RESTClient(api_key="API_KEY")

# create request options
options = RequestOptionBuilder().edge_headers(
    edge_id="YOUR_EDGE_ID",  # required
    edge_ip_address="IP_ADDRESS",  # required
)
```
Request data using client methods.
```python
# get response
res = c.get_aggs("AAPL", 1, "day", "2022-04-04", "2022-04-04", options=options)

# do something with response
```
Checkout Launchpad readme for more details on RequestOptionBuilder [here](./examples/launchpad)


## Contributing

If you found a bug or have an idea for a new feature, please first discuss it with us by
[submitting a new issue](https://github.com/polygon-io/client-python/issues/new/choose).
We will respond to issues within at most 3 weeks.
We're also open to volunteers if you want to submit a PR for any open issues but
please discuss it with us beforehand. PRs that aren't linked to an existing issue or
discussed with us ahead of time will generally be declined. If you have more general
feedback or want to discuss using this client with other users, feel free to reach out
on our [Slack channel](https://polygon-io.slack.com/archives/C03FRFN7UF3).

### Development

If you plan to contribute by developing new features then you will need to install certain dependencies.

#### Poetry

Poetry is a packaging and dependency manager for Python.
Installation instructions can be found [on their website](https://python-poetry.org/docs/#installation).
Once installed run `poetry install` to install the required dependencies. This step should be run after incorporating new upstream changes.

#### Makefile

Our Makefile has the common operations needed when developing on this repo. Running tests and linting can both be run through our Makefile. Just run `make help` to see the list of available commands. 

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
