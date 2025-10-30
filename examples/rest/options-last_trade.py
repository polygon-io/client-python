from massive import RESTClient

# docs
# https://massive.com/docs/options/get_v2_last_trade__optionsticker
# https://massive-api-client.readthedocs.io/en/latest/Trades.html#get-last-trade

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

trade = client.get_last_trade(
    "O:TSLA210903C00700000",
)

print(trade)
