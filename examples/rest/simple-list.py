from massive import RESTClient

client = RESTClient()

trades = []
for t in client.list_trades("AAA", "2022-04-04", limit=5):
    trades.append(t)
print(trades)
