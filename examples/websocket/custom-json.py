from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List
from examples import custom_json

c = WebSocketClient(subscriptions=["T.*"], custom_json=custom_json)


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)


c.run(handle_msg)
