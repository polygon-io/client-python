from massive import RESTClient

# docs
# https://massive.com/docs/indices/get_v3_snapshot_indices
# https://github.com/massive-com/client-python/blob/master/massive/rest/snapshot.py#

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

tickers = ["I:SPX", "I:DJI", "I:VIX"]
snapshot = client.get_snapshot_indices(tickers)

# print raw values
print(snapshot)
