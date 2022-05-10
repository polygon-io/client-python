from polygon import RESTClient
from datetime import date, datetime

client = RESTClient(verbose=True)

aggs1 = client.get_aggs(
    ticker="AAPL", multiplier=1, timespan="day", from_="2005-04-04", to="2005-04-04"
)
aggs2 = client.get_aggs(
    ticker="AAPL",
    multiplier=1,
    timespan="day",
    from_=date(2005, 4, 4),
    to=datetime(2005, 4, 4),
)

if aggs1 != aggs2:
    print(aggs1, aggs2)
    assert False
else:
    print(aggs1)
