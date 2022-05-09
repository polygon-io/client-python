from polygon import RESTClient
from datetime import date, datetime

client = RESTClient(verbose=True)

aggs = client.get_aggs("AAPL", 1, "day", "2005-04-04", "2005-04-04")
print(aggs)
aggs = client.get_aggs("AAPL", 1, "day", date(2005, 4, 4), datetime(2005, 4, 4))
print(aggs)
details = client.get_ticker_details('AAPL')
print(details)
