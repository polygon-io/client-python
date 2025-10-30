from massive import RESTClient

# docs
# https://massive.com/docs/crypto/get_v1_last_crypto__from___to
# https://massive-api-client.readthedocs.io/en/latest/Trades.html#get-last-crypto-trade

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

trade = client.get_last_crypto_trade("BTC", "USD")

print(trade)
