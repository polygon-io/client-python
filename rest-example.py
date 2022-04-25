from polygon import RESTClient
from polygon.rest.models import Sort

c = RESTClient()

aggs = c.get_aggs("AAPL", 1, "day", "2005-04-01", "2005-04-04")
print(aggs)

trades = []
for t in c.list_trades("AAA", timestamp="2022-04-20", limit=5, sort=Sort.ASC):
    trades.append(t)
print(trades)
