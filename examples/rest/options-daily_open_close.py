from polygon import RESTClient

# docs
# https://polygon.io/docs/options/get_v1_open-close__optionsticker___date
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#get-daily-open-close-agg

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

# make request
request = client.get_daily_open_close_agg(
    "O:SPY251219C00650000",
    "2023-02-22",
)

print(request)
