from massive import WebSocketClient
from massive.websocket.models import WebSocketMessage, EquityTrade
from typing import List

c = WebSocketClient(subscriptions=["T.*"])


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
