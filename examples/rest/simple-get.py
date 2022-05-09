from polygon import RESTClient
from datetime import date, datetime

client = RESTClient(verbose=True)

aggs1 = client.get_aggs("AAPL", 1, "day", "2005-04-04", "2005-04-04")
aggs2 = client.get_aggs("AAPL", 1, "day", date(2005, 4, 4), datetime(2005, 4, 4))

if aggs1 != aggs2:
    print(aggs1, aggs2)
    assert(False)
else:
    print(aggs1)

