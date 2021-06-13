[![Build Status](https://drone.polygon.io/api/badges/polygon-io/client-python/status.svg)](https://drone.polygon.io/polygon-io/client-python)
[![PyPI version](https://badge.fury.io/py/polygon-api-client.svg)](https://badge.fury.io/py/polygon-api-client)

# Polygon Python Client - WebSocket & RESTful APIs

Python client for the Polygon.io [Stocks API](https://polygon.io)

## Getting Started

For a basic product overview, check out our [setup and use documentation](https://polygon.io/sockets)

### Install

`pip install polygon-api-client`

`polygon-api-client` supports python version >= 3.6

## Simple WebSocket Demo
```python
import time

from polygon import WebSocketClient, STOCKS_CLUSTER


def my_custom_process_message(message):
    print("this is my custom message processing", message)


def my_custom_error_handler(ws, error):
    print("this is my custom error handler", error)


def my_custom_close_handler(ws):
    print("this is my custom close handler")


def main():
    key = 'your api key'
    my_client = WebSocketClient(STOCKS_CLUSTER, key, my_custom_process_message)
    my_client.run_async()

    my_client.subscribe("T.MSFT", "T.AAPL", "T.AMD", "T.NVDA")
    time.sleep(1)

    my_client.close_connection()


if __name__ == "__main__":
    main()
```

## Simple REST Demo
```python
from polygon import RESTClient


def main():
    key = "your api key"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        resp = client.stocks_equities_daily_open_close("AAPL", "2021-03-02")
        print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")


if __name__ == '__main__':
    main()

```

### Query parameters for REST calls

Every function call under our RESTClient has the `query_params` kwargs. These kwargs are passed along and mapped 1:1
as query parameters to the underling HTTP call. For more information on the different query parameters please reference
our [API Docs](https://polygon.io/docs/).

#### Example with query parameters

```python
import datetime

from polygon import RESTClient


def ts_to_datetime(ts) -> str:
    return datetime.datetime.fromtimestamp(ts / 1000.0).strftime('%Y-%m-%d %H:%M')


def main():
    key = "your api key"

    # RESTClient can be used as a context manager to facilitate closing the underlying http session
    # https://requests.readthedocs.io/en/master/user/advanced/#session-objects
    with RESTClient(key) as client:
        from_ = "2019-01-01"
        to = "2019-02-01"
        resp = client.stocks_equities_aggregates("AAPL", 1, "minute", from_, to, unadjusted=False)

        print(f"Minute aggregates for {resp.ticker} between {from_} and {to}.")

        for result in resp.results:
            dt = ts_to_datetime(result["t"])
            print(f"{dt}\n\tO: {result['o']}\n\tH: {result['h']}\n\tL: {result['l']}\n\tC: {result['c']} ")


if __name__ == '__main__':
    main()
```  

## Notes about the REST Client

We use swagger as our API spec and we used this swagger to generate most of the code that defines the REST client.
We made this decision due to the size of our API, many endpoints and object definitions, and to accommodate future changes.

