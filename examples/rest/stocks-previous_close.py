from massive import RESTClient

# docs
# https://massive.com/docs/stocks/get_v2_aggs_ticker__stocksticker__prev
# https://massive-api-client.readthedocs.io/en/latest/Aggs.html#get-previous-close-agg

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

aggs = client.get_previous_close_agg(
    "AAPL",
)

print(aggs)
