from polygon import RESTClient
from polygon.rest.models import (
    TickerSnapshot,
    Agg,
)

# docs
# https://polygon.io/docs/crypto/get_v2_snapshot_locale_global_markets_crypto_tickers
# https://polygon-api-client.readthedocs.io/en/latest/Snapshot.html#get-all-snapshots

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

snapshot = client.get_snapshot_all("crypto")  # all tickers

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
