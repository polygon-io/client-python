from polygon import RESTClient

# docs
# https://polygon.io/docs/stocks/get_v2_last_trade__stocksticker
# https://polygon-api-client.readthedocs.io/en/latest/Trades.html#get-last-trade

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

trade = client.get_last_trade(
    "AAPL",
)

print(trade)
