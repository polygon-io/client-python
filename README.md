[![PyPI version](https://badge.fury.io/py/polygon-api-client.svg)](https://badge.fury.io/py/polygon-api-client)
[![Docs](https://readthedocs.org/projects/polygon-api-client/badge/?version=latest)](https://polygon-api-client.readthedocs.io/en/latest/)

# Polygon Python Client - WebSocket & RESTful APIs

Python client for the Polygon.io [Stocks API](https://polygon.io)

## Getting Started

For a basic product overview, check out our [setup and use documentation](https://polygon.io/sockets)

### Install

Requires python version >= 3.7

`pip install polygon-api-client`

## REST Demos
### Getting aggs
```python
from polygon import RESTClient

client = RESTClient() # Uses POLYGON_API_KEY env var. Can optionally supply your key as first parameter.
aggs = client.get_aggs("AAPL", 1, "day", "2005-04-01", "2005-04-04")
```

### Getting trades
```python
from polygon import RESTClient
from polygon.rest.models import Sort

client = RESTClient() # Uses POLYGON_API_KEY env var. Can optionally supply your key as first parameter.

trades = []
for t in client.list_trades("AAA", timestamp="2022-04-20", limit=5, sort=Sort.ASC):
    trades.append(t)
```

### Getting raw response
To handle the raw [urllib3 response](https://urllib3.readthedocs.io/en/stable/reference/urllib3.response.html?highlight=response#response) yourself, pass `raw=True`.
