from massive import WebSocketClient
from massive.websocket.models import WebSocketMessage, EquityQuote
from typing import List, cast
import time

c = WebSocketClient(subscriptions=["Q.SPY"])


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        q: EquityQuote = cast(EquityQuote, m)
        if q.timestamp is not None:
            now = time.time() * 1000
            print(now, q.timestamp, now - q.timestamp)


c.run(handle_msg)
