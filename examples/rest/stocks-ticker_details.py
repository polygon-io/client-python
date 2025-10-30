from massive import RESTClient

# docs
# https://massive.com/docs/stocks/get_v3_reference_tickers__ticker
# https://massive-api-client.readthedocs.io/en/latest/Reference.html#get-ticker-details

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

details = client.get_ticker_details("AAPL")
print(details)
