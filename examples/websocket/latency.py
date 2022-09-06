from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List
import time

c = WebSocketClient(subscriptions=["Q.SPY"])


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        now = time.time() * 1000
        print(now, m.timestamp, now - m.timestamp)


c.run(handle_msg)
