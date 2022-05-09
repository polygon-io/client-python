from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage, Market
from typing import List

c = WebSocketClient(market=Market.Crypto, subscriptions=['XT.*'])

def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)

c.run(handle_msg)
