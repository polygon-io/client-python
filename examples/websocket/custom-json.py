from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List

# type: ignore
import orjson

c = WebSocketClient(subscriptions=["T.*"], custom_json=orjson)


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)


c.run(handle_msg)
