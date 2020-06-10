[![Build Status](https://drone.polygon.io/api/badges/polygon-io/client-python/status.svg)](https://drone.polygon.io/polygon-io/client-python)

# Polygon Python Client - WebSocket & RESTful APIs

Python client for the [Polygon.io API](polygon.io)

## Getting Started

For a basic product overview, check out our [setup and use documentation](https://polygon.io/sockets)

### Install

`pip install polygon-api-client`

`polygon-api-client` supports python version >= 3.6

## Simple WebSocket Demo
```python
import time


from polygon import WebSocketClient, STOCKS_CLUSTER


def my_customer_process_message(message):
    print("this is my custom message processing", message)


def main():
    key = 'your api key'
    my_client = WebSocketClient(STOCKS_CLUSTER, key, my_customer_process_message)
    my_client.run_async()

    my_client.subscribe("T.MSFT", "T.AAPL", "T.AMD", "T.NVDA")
    time.sleep(2)

    my_client.close_connection()


if __name__ == "__main__":
    main()

```

## Simple REST Demo
```python
from polygon import RESTClient


def main():
    key = "your api key"
    client = RESTClient(key)

    resp = client.stocks_equities_daily_open_close("AAPL", "2018-3-2")
    print(f"On: {resp.from_} Apple opened at {resp.open} and closed at {resp.close}")


if __name__ == '__main__':
    main()
```


## Notes about the REST Client

We use swagger as our API spec and we used this swagger to generate most of the code that defines the REST client.
We made this decision due to the size of our API, many endpoints and object definitions, and to accommodate future changes.

