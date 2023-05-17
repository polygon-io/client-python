from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List

# client = WebSocketClient("XXXXXX") # hardcoded api_key is used
client = WebSocketClient()  # POLYGON_API_KEY environment variable is used

# docs
# https://polygon.io/docs/stocks/ws_stocks_am
# https://polygon-api-client.readthedocs.io/en/latest/WebSocket.html#

# aggregates (per minute)
# client.subscribe("AM.*") # all aggregates
# client.subscribe("AM.TSLA") # single ticker

# aggregates (per second)
client.subscribe("A.*")  # all aggregates
# client.subscribe("A.TSLA") # single ticker

# trades
# client.subscribe("T.*")  # all trades
# client.subscribe("T.TSLA", "T.UBER") # multiple tickers

# quotes
# client.subscribe("Q.*")  # all quotes
# client.subscribe("Q.TSLA", "Q.UBER") # multiple tickers


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        print(m)


# print messages
client.run(handle_msg)
