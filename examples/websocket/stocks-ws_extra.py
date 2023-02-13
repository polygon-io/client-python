from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage
from typing import List
from typing import Dict
import time
import threading


# docs
# https://polygon.io/docs/stocks/ws_stocks_am
# https://polygon-api-client.readthedocs.io/en/latest/WebSocket.html#

# aggregates
# client.subscribe("AM.*") # aggregates (per minute)
# client.subscribe("A.*") # aggregates (per second)

# trades
# client.subscribe("T.*") # all trades
# client.subscribe("T.TSLA", "T.UBER") # limited trades

# quotes
# client.subscribe("Q.*") # all quotes
# client.subscribe("Q.TSLA", "Q.UBER") # limited quotes


def run_websocket_client():
    # client = WebSocketClient("XXXXXX") # hardcoded api_key is used
    client = WebSocketClient()  # POLYGON_API_KEY environment variable is used
    client.subscribe("T.*")  # all trades
    client.run(handle_msg)


string_map: Dict[str, int]
string_map = {}  #


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        # print(m)

        # verify this is a string
        if isinstance(m, str):

            if m.symbol in string_map:
                string_map[m.symbol] += 1
            else:
                string_map[m.symbol] = 1


# print messages
# client.run(handle_msg)


def your_function():
    sorted_string_map = sorted(string_map.items(), key=lambda x: x[1], reverse=True)
    print("\033c", end="")  # ANSI escape sequence to clear the screen
    # print(sorted_string_map[:10])
    for index, item in sorted_string_map[:10]:
        print("{:<15}{:<15}".format(index, item))
    string_map.clear()  # reset
    # print()


def run_function_periodically():
    while True:
        your_function()
        time.sleep(5)


thread1 = threading.Thread(target=run_function_periodically)
thread2 = threading.Thread(target=run_websocket_client)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
