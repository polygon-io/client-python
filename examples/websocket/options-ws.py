from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage, Market
from typing import List

# docs
# https://polygon.io/docs/options/ws_getting-started
# https://polygon-api-client.readthedocs.io/en/latest/WebSocket.html

# client = WebSocketClient("XXXXXX") # hardcoded api_key is used
client = WebSocketClient(
    market=Market.Options
)  # POLYGON_API_KEY environment variable is used

# aggregates
# client.subscribe("AM.*") # aggregates (per minute)
client.subscribe("A.*")  # aggregates (per second)

# trades
# client.subscribe("T.*") # all trades
# client.subscribe("T.O:SPY241220P00720000", "T.O:SPY251219C00650000") # limited trades

# quotes (1,000 option contracts per connection)
# client.subscribe("Q.O:SPY241220P00720000", "Q.O:SPY251219C00650000") # limited quotes


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)


# print messages
client.run(handle_msg)
