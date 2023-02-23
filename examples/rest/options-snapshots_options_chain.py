from polygon import RESTClient

# docs
# https://polygon.io/docs/options/get_v3_snapshot_options__underlyingasset
# ttps://polygon-api-client.readthedocs.io/en/latest/Snapshot.html#get-all-snapshots

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

options_chain = []
for o in client.list_snapshot_options_chain("HCP"):
    options_chain.append(o)
print(options_chain)
