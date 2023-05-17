from polygon import RESTClient

# docs
# https://polygon.io/docs/options/get_v3_snapshot_options__underlyingasset___optioncontract
# https://polygon-api-client.readthedocs.io/en/latest/Snapshot.html

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

snapshot = client.get_snapshot_option("AAPL", "O:AAPL230616C00150000")

# print raw values
print(snapshot)
