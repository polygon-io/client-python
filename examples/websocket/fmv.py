from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage, Feed, Market
from typing import List

client = WebSocketClient(feed=Feed.Business, market=Market.Stocks, verbose=True)

# Aggregates (per minute)
client.subscribe("FMV.*")  # all ticker symbols
# client.subscribe("XA.BTC-USD")
# client.subscribe("XA.BTC-EUR")
# client.subscribe("XA.ETH-USD")

def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)


client.run(handle_msg)
