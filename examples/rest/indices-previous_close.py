from polygon import RESTClient

# docs
# https://polygon.io/docs/indices/get_v2_aggs_ticker__indicesticker__prev
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#get-previous-close-agg

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

aggs = client.get_previous_close_agg(
    "I:SPX",
)

print(aggs)
