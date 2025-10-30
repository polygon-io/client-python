from massive import RESTClient

# docs
# https://massive.com/docs/crypto/get_v3_trades__cryptoticker
# https://massive-api-client.readthedocs.io/en/latest/Trades.html#massive.RESTClient.list_trades

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

trades = []
for t in client.list_trades("X:BTC-USD", "2023-02-01", limit=50000):
    trades.append(t)

# prints each trade that took place
print(trades)
