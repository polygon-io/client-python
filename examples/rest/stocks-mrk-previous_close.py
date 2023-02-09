from polygon import RESTClient

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v2_aggs_ticker__stocksticker__prev
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#get-previous-close-agg

aggs = client.get_previous_close_agg(
    "AAPL",
)

print(aggs)
