from polygon import RESTClient

# docs
# https://polygon.io/docs/forex/get_v2_aggs_ticker__forexticker__prev
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#get-previous-close-agg

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

aggs = client.get_previous_close_agg(
    "C:EURUSD",
)

print(aggs)
