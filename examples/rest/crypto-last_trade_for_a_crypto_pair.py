from polygon import RESTClient

# docs
# https://polygon.io/docs/crypto/get_v1_last_crypto__from___to
# https://polygon-api-client.readthedocs.io/en/latest/Trades.html#get-last-crypto-trade

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

trade = client.get_last_crypto_trade(
    "BTC",
    "USD"
)

print(trade)
