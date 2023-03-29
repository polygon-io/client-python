from polygon import RESTClient

# docs
# https://polygon.io/docs/indices/get_v3_snapshot_indices
# https://github.com/polygon-io/client-python/blob/master/polygon/rest/snapshot.py#

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

snapshot = client.get_snapshot_indices("I:SPX")

# print raw values
print(snapshot)
