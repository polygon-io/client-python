from polygon import RESTClient

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v2_snapshot_locale_us_markets_stocks__direction
# https://polygon-api-client.readthedocs.io/en/latest/Snapshot.html#get-gainers-losers-snapshot

# get gainers
gainers = client.get_snapshot_direction("stocks", "gainers")
# print(gainers)

# print ticker with % change
for item in gainers:
    print("{:<15}{:.2f} %".format(item.ticker, item.todays_change_percent))

print()

# get losers
losers = client.get_snapshot_direction("stocks", "losers")
# print(losers)

# print ticker with % change
for item in losers:
    print("{:<15}{:.2f} %".format(item.ticker, item.todays_change_percent))
