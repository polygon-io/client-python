from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List

client = WebSocketClient("N_4QqOFs3X_pCHeIJjW4pCETSOBerS4_") # api_key is used

# docs
# https://polygon.io/docs/stocks/ws_stocks_am
# https://polygon-api-client.readthedocs.io/en/latest/WebSocket.html#

# aggregates
#client.subscribe("AM.*") # aggregates (per minute)
#client.subscribe("A.*") # aggregates (per second)

# trades
#client.subscribe("T.*") # all trades
#client.subscribe("T.TSLA", "T.UBER") # limited trades

# quotes
#client.subscribe("Q.*") # all quotes
#client.subscribe("Q.TSLA", "Q.UBER") # limited quotes


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)

# print messages
client.run(handle_msg)
