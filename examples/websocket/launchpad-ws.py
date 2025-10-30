from massive import WebSocketClient
from massive.websocket.models import WebSocketMessage, Feed, Market
from typing import List

client = WebSocketClient(
    api_key="<MASSIVE_API_KEY>", feed=Feed.Launchpad, market=Market.Stocks
)

client.subscribe("AM.*")  # all aggregates
# client.subscribe("LV.*")  # all aggregates
# client.subscribe("AM.O:A230616C00070000")  # all aggregates
# client.subscribe("LV.O:A230616C00070000")  # all aggregates


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)


# print messages
client.run(handle_msg)
