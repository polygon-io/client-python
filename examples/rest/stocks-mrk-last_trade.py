from polygon import RESTClient

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v2_last_trade__stocksticker
# https://polygon-api-client.readthedocs.io/en/latest/Trades.html#get-last-trade

trade = client.get_last_trade(
    "AAPL",
)

print(trade)
