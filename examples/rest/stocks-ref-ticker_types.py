from polygon import RESTClient

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v3_reference_tickers_types
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-ticker-types

types = client.get_ticker_types()
print(types)
