from massive import WebSocketClient
from massive.websocket.models import WebSocketMessage, Feed, Market
from typing import List

client = WebSocketClient(feed=Feed.Business, market=Market.Stocks, verbose=True)

# FMV
client.subscribe("FMV.*")  # all ticker symbols
# client.subscribe("FMV.TSLA")
# client.subscribe("FMV.AAPL")
# client.subscribe("FMV.NVDA")


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)


client.run(handle_msg)
