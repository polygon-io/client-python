from massive import RESTClient
from massive.rest.models import (
    TickerSnapshot,
)

# docs
# https://massive.com/docs/stocks/get_v2_snapshot_locale_us_markets_stocks__direction
# https://massive-api-client.readthedocs.io/en/latest/Snapshot.html#get-gainers-losers-snapshot

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

# get gainers
gainers = client.get_snapshot_direction("stocks", "gainers")
# print(gainers)

# print ticker with % change
for gainer in gainers:
    # verify this is a TickerSnapshot
    if isinstance(gainer, TickerSnapshot):
        # verify this is a float
        if isinstance(gainer.todays_change_percent, float):
            print("{:<15}{:.2f} %".format(gainer.ticker, gainer.todays_change_percent))

print()

# get losers
losers = client.get_snapshot_direction("stocks", "losers")
# print(losers)

# print ticker with % change
for loser in losers:
    # verify this is a TickerSnapshot
    if isinstance(loser, TickerSnapshot):
        # verify this is a float
        if isinstance(loser.todays_change_percent, float):
            print("{:<15}{:.2f} %".format(loser.ticker, loser.todays_change_percent))
