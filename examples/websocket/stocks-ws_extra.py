from polygon import WebSocketClient
from polygon.websocket.models import WebSocketMessage, EquityTrade
from typing import List
from typing import Dict
from datetime import datetime
import time
import threading

# docs
# https://polygon.io/docs/stocks/ws_stocks_am
# https://polygon-api-client.readthedocs.io/en/latest/WebSocket.html#

# This program connects to the Polygon WebSocket API, authenticates the
# connection, and subscribes to receive trades. Every 5 seconds, it counts
# the number of trades per symbol and stores the results in a map. The
# program then prints the map, which gives a readout of the top stocks
# traded in the past 5 seconds.


def run_websocket_client():
    # client = WebSocketClient("XXXXXX") # hardcoded api_key is used
    client = WebSocketClient()  # POLYGON_API_KEY environment variable is used
    client.subscribe("T.*")  # all trades
    client.run(handle_msg)


string_map: Dict[str, int]
string_map = {}  #
cash_traded = float(0)


def handle_msg(msgs: List[WebSocketMessage]):
    for m in msgs:
        # print(m)

        if type(m) == EquityTrade:
            # verify this is a string
            if isinstance(m.symbol, str):
                if m.symbol in string_map:
                    string_map[m.symbol] += 1
                else:
                    string_map[m.symbol] = 1

            # verify these are float
            if isinstance(m.price, float) and isinstance(m.size, int):
                global cash_traded
                cash_traded += m.price * m.size
                # print(cash_traded)


def top_function():
    # start timer
    start_time = time.time()

    sorted_string_map = sorted(string_map.items(), key=lambda x: x[1], reverse=True)
    print("\033c", end="")  # ANSI escape sequence to clear the screen

    for index, item in sorted_string_map[:25]:
        print("{:<15}{:<15}".format(index, item))

    # end timer
    end_time = time.time()

    # print stats
    print()

    # current time
    current_time = datetime.now()
    print(f"Time: {current_time}")

    # how many tickers seen
    ticker_count = len(sorted_string_map)
    print(f"Tickers seen: {ticker_count}")

    # how many trades seen
    trade_count = 0
    for index, item in sorted_string_map:
        trade_count += item
    print(f"Trades seen: {trade_count}")

    # cash traded
    global cash_traded
    formatted_number = "{:,.2f}".format(cash_traded)
    print("Roughly " + formatted_number + " cash changed hands")

    # performance?
    print(f"Time taken: {end_time - start_time:.6f} seconds")

    # clear map and cash for next loop
    string_map.clear()
    cash_traded = 0


def run_function_periodically():
    while True:
        top_function()
        time.sleep(5)


thread1 = threading.Thread(target=run_function_periodically)
thread2 = threading.Thread(target=run_websocket_client)

thread1.start()
thread2.start()

thread1.join()
thread2.join()
