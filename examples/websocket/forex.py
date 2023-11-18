from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage, Market
from typing import List

client = WebSocketClient(market=Market.Forex)

# Aggregates (per minute)
# client.subscribe("CA.*") # all forex pair
client.subscribe("CA.USD/CAD")
client.subscribe("CA.USD/EUR")
client.subscribe("CA.USD/AUD")

# Aggregates (per second)
# client.subscribe("CAS.*") # all forex pair
# client.subscribe("CAS.USD/CAD")
# client.subscribe("CAS.USD/EUR")
# client.subscribe("CAS.USD/AUD")

# Quotes
# client.subscribe("C.*") # all forex pair
# client.subscribe("C.USD/CAD")
# client.subscribe("C.USD/EUR")
# client.subscribe("C.USD/AUD")


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)


client.run(handle_msg)
