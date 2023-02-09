from polygon import RESTClient

#client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX") # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v3_reference_splits
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#list-splits

splits = []
for s in client.list_splits("TSLA", limit=1000):
    splits.append(s)
print(splits)