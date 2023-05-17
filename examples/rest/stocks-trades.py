from polygon import RESTClient

# docs
# https://polygon.io/docs/stocks/get_v3_trades__stockticker
# https://polygon-api-client.readthedocs.io/en/latest/Trades.html#polygon.RESTClient.list_trades

# Trade data refers to the tick records of individual transactions that have
# taken place in a financial market, such as the price, size, and time of
# each trade. It provides a high-frequency, granular view of market activity,
# and is used by traders, investors, and researchers to gain insights into
# market behavior and inform their investment decisions.

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

trades = []
for t in client.list_trades("IBIO", "2023-02-01", limit=50000):
    trades.append(t)

# prints each trade that took place
print(trades)
