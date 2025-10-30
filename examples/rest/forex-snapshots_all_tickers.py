from massive import RESTClient
from massive.rest.models import (
    TickerSnapshot,
    Agg,
)

# docs
# https://massive.com/docs/forex/get_v2_snapshot_locale_global_markets_forex_tickers
# https://massive-api-client.readthedocs.io/en/latest/Snapshot.html#get-all-snapshots

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

snapshot = client.get_snapshot_all("forex")  # all tickers

# print raw values
print(snapshot)

# crunch some numbers
for item in snapshot:
    # verify this is an TickerSnapshot
    if isinstance(item, TickerSnapshot):
        # verify this is an Agg
        if isinstance(item.prev_day, Agg):
            # verify this is a float
            if isinstance(item.prev_day.open, float) and isinstance(
                item.prev_day.close, float
            ):
                percent_change = (
                    (item.prev_day.close - item.prev_day.open)
                    / item.prev_day.open
                    * 100
                )
                print(
                    "{:<15}{:<15}{:<15}{:.2f} %".format(
                        item.ticker,
                        item.prev_day.open,
                        item.prev_day.close,
                        percent_change,
                    )
                )
