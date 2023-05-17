from polygon import RESTClient

# docs
# https://polygon.io/docs/stocks/get_v3_reference_tickers__ticker
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-ticker-details

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

details = client.get_ticker_details("AAPL")
print(details)
