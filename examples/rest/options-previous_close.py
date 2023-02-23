from polygon import RESTClient

# docs
# https://polygon.io/docs/options/get_v2_aggs_ticker__optionsticker__prev
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#get-previous-close-agg

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

aggs = client.get_previous_close_agg(
    "O:SPY251219C00650000",
)

print(aggs)
