from massive import RESTClient

# docs
# https://massive.com/docs/options/get_v3_trades__optionsticker
# https://massive-api-client.readthedocs.io/en/latest/Trades.html#massive.RESTClient.list_trades

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

trades = []
for t in client.list_trades("O:TSLA210903C00700000", limit=50000):
    trades.append(t)

# prints each trade that took place
print(trades)
