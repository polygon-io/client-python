[![PyPI version](https://badge.fury.io/py/polygon-api-client.svg)](https://badge.fury.io/py/polygon-api-client)
[![Docs](https://readthedocs.org/projects/polygon-api-client/badge/?version=latest)](https://polygon-api-client.readthedocs.io/en/latest/)

# Polygon Python Client - WebSocket & RESTful APIs

Python client for the [Polygon.io API](https://polygon.io).

## Install

`pip install polygon-api-client`

Requires python version >= 3.7

## REST getting started
### Getting aggs
```python
from polygon import RESTClient

client = RESTClient() # Uses POLYGON_API_KEY env var. Can optionally supply your key.
aggs = client.get_aggs("AAPL", 1, "day", "2005-04-01", "2005-04-04")
```

### Getting trades
```python
from polygon import RESTClient
from polygon.rest.models import Sort

client = RESTClient() # Uses POLYGON_API_KEY env var. Can optionally supply your key.

trades = []
for t in client.list_trades("AAA", timestamp="2022-04-20", limit=5, sort=Sort.ASC):
    trades.append(t)
```

### Getting raw response
To handle the raw [urllib3 response](https://urllib3.readthedocs.io/en/stable/reference/urllib3.response.html?highlight=response#response) yourself, pass `raw=True`:

```python
from polygon import RESTClient

client = RESTClient() # Uses POLYGON_API_KEY env var. Can optionally supply your key.
response = client.get_aggs("AAPL", 1, "day", "2005-04-01", "2005-04-04", raw=True)
```

## WebSocket getting started

### Simple synchronous callback
```python
from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List

c = WebSocketClient(subscriptions=['T.AAPL']) # Uses POLYGON_API_KEY env var. Can optionally supply your key.

def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)

c.run(handle_msg)
```

### Synchronous aggregates
```python
from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List

class MessageHandler:
    count = 0

    def handle_msg(self, msgs: List[WebSocketMessage]):
        for m in msgs:
            if type(m) == EquityTrade:
                print(self.count, m)
                self.count += 1

h = MessageHandler()

def handle_msg(msgs: List[WebSocketMessage]):
    h.handle_msg(msgs)

c.run(handle_msg)
```

### Asynchronous callback
```python
from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List

c = WebSocketClient(subscriptions=['T.AAPL']) # Uses POLYGON_API_KEY env var. Can optionally supply your key.

async def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)

async def timeout():
    await asyncio.sleep(1)
    print('unsubscribe_all')
    c.unsubscribe_all()
    await asyncio.sleep(1)
    print('close')
    await c.close()

async def main():
    await asyncio.gather(
        c.connect(handle_msg),
        timeout()
    )

asyncio.run(main())
```

### Getting raw response
```python
from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import Union
import json

c = WebSocketClient(subscriptions=['T.*'], raw=True)

def handle_msg(msgs: Union[str, bytes]):
		print(json.loads(msgs))

c.run(handle_msg)
```
