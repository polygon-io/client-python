from polygon import RESTClient

# docs
# https://polygon.io/docs/crypto/get_v2_aggs_ticker__cryptoticker__prev
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#get-previous-close-agg

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

aggs = client.get_previous_close_agg(
    "X:BTCUSD",
)

print(aggs)
