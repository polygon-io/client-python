from massive import WebSocketClient
from massive.websocket.models import WebSocketMessage
from typing import List

# client = WebSocketClient("XXXXXX") # hardcoded api_key is used
client = WebSocketClient()  # MASSIVE_API_KEY environment variable is used

# docs
# https://massive.com/docs/stocks/ws_stocks_am
# https://massive-api-client.readthedocs.io/en/latest/WebSocket.html#

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
