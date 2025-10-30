from massive import RESTClient

# docs
# https://massive.com/docs/stocks/get_v3_reference_tickers_types
# https://massive-api-client.readthedocs.io/en/latest/Reference.html#get-ticker-types

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

types = client.get_ticker_types()
print(types)
