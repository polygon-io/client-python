from massive import RESTClient

# docs
# https://massive.com/docs/forex/get_v1_conversion__from___to
# https://massive-api-client.readthedocs.io/en/latest/Quotes.html#get-real-time-currency-conversion

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

rate = client.get_real_time_currency_conversion(
    "AUD",
    "USD",
)

print(rate)
