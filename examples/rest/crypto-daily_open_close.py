from polygon import RESTClient

# docs
# https://polygon.io/docs/crypto/get_v1_open-close_crypto__from___to___date
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#get-daily-open-close-agg

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

# make request
request = client.get_daily_open_close_agg(
    "X:BTCUSD",
    "2023-01-09",
)

print(request)
