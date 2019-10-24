# A Python client library for Polgyon's WebSocket and RESTful APIs

Currently this repo only supports the WebSocket API

## Getting Started

For a basic product overview, check out our [setup and use documentation](https://polygon.io/sockets)


## Simple Demo
```python
import time


from polygon_client import WebSocketClient, STOCKS_CLUSTER


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
