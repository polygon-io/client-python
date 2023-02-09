from polygon import RESTClient

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v1_open-close__stocksticker___date
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#get-daily-open-close-agg

# make request
request = client.get_daily_open_close_agg(
    "AAPL",
    "2023-02-07",
)

print(request)
