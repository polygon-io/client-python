from polygon import RESTClient
from polygon.rest.models import Sort

client = RESTClient(verbose=True)

aggs = client.get_aggs("AAPL", 1, "day", "2005-04-01", "2005-04-04")
print(aggs)

trades = []
for t in client.list_trades("AAA", timestamp="2022-04-20", limit=5, sort=Sort.ASC):
    trades.append(t)
print(trades)

print(client.list_trades("AAA", timestamp="2022-04-20", limit=5, raw=True))
