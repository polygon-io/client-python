from polygon import RESTClient

# docs
# https://polygon.io/docs/stocks/get_v3_reference_tickers_types
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-ticker-types

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

types = client.get_ticker_types()
print(types)
