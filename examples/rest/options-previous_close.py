from massive import RESTClient

# docs
# https://massive.com/docs/options/get_v2_aggs_ticker__optionsticker__prev
# https://massive-api-client.readthedocs.io/en/latest/Aggs.html#get-previous-close-agg

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

aggs = client.get_previous_close_agg(
    "O:SPY251219C00650000",
)

print(aggs)
