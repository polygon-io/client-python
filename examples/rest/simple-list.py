from polygon import RESTClient

client = RESTClient(verbose=True)

trades = []
for t in client.list_trades("AAA", timestamp="2022-04-20", limit=5):
    trades.append(t)
print(trades)
