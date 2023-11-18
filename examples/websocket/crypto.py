from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage, Market
from typing import List

client = WebSocketClient(market=Market.Crypto)

# Aggregates (per minute)
client.subscribe("XA.*") # all crypto pair
# client.subscribe("XA.BTC-USD")
# client.subscribe("XA.BTC-EUR")
# client.subscribe("XA.ETH-USD")

# Aggregates (per second)
# client.subscribe("XAS.*") # all crypto pair
# client.subscribe("XAS.BTC-USD")
# client.subscribe("XAS.BTC-EUR")
# client.subscribe("XAS.ETH-USD")

# Trades
# client.subscribe("XT.*") # all crypto pair
# client.subscribe("XT.BTC-USD")
# client.subscribe("XT.BTC-EUR")
# client.subscribe("XT.ETH-USD")

# Quotes
# client.subscribe("XQ.*") # all crypto pair
# client.subscribe("XQ.BTC-USD")
# client.subscribe("XQ.BTC-EUR")
# client.subscribe("XQ.ETH-USD")

# Level 2 Book
# client.subscribe("XL2.*") # all crypto pair
# client.subscribe("XL2.BTC-USD")
# client.subscribe("XL2.BTC-EUR")
# client.subscribe("XL2.ETH-USD")

def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)


client.run(handle_msg)
