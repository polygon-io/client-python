from polygon import RESTClient

# docs
# https://polygon.io/docs/stocks/get_v3_reference_splits
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#list-splits

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

splits = []
for s in client.list_splits("TSLA", limit=1000):
    splits.append(s)
print(splits)
