from massive import RESTClient

# docs
# https://massive.com/docs/stocks/get_v3_reference_splits
# https://massive-api-client.readthedocs.io/en/latest/Reference.html#list-splits

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

splits = []
for s in client.list_splits("TSLA", limit=1000):
    splits.append(s)
print(splits)
