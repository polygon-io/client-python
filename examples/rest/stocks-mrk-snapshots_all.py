from polygon import RESTClient
from polygon.rest.models import (
    TickerSnapshot,
    Agg,
)

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v2_snapshot_locale_us_markets_stocks_tickers
# https://polygon-api-client.readthedocs.io/en/latest/Snapshot.html#get-all-snapshots

# tickers we are interested in
tickers = ["TSLA", "AAPL", "MSFT", "META"]

# snapshot = client.get_snapshot_all("stocks") # all tickers
snapshot = client.get_snapshot_all("stocks", tickers)

# print raw values
print(snapshot)

# crunch some numbers
for item in snapshot:

    percent_change = (
        (item.prev_day.close - item.prev_day.open) / item.prev_day.open * 100
    )
    print(
        "{:<15}{:<15}{:<15}{:.2f} %".format(
            item.ticker, item.prev_day.open, item.prev_day.close, percent_change
        )
    )
