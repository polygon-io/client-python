from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List

c = WebSocketClient(subscriptions=["T.*"])


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)


c.run(handle_msg)
