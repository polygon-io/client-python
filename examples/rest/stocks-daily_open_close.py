from massive import RESTClient

# docs
# https://massive.com/docs/stocks/get_v1_open-close__stocksticker___date
# https://massive-api-client.readthedocs.io/en/latest/Aggs.html#get-daily-open-close-agg

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

# make request
request = client.get_daily_open_close_agg(
    "AAPL",
    "2023-02-07",
)

print(request)
