from polygon import RESTClient

# docs
# https://polygon.io/docs/forex/get_v1_conversion__from___to
# https://polygon-api-client.readthedocs.io/en/latest/Quotes.html#get-real-time-currency-conversion

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

rate = client.get_real_time_currency_conversion(
    "AUD",
    "USD",
)

print(rate)
