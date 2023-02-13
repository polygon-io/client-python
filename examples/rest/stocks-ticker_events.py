from polygon import RESTClient

# docs
# https://polygon.io/docs/stocks/get_vx_reference_tickers__id__events
# https://github.com/polygon-io/client-python/blob/master/polygon/rest/reference.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

events = client.get_ticker_events("META")
print(events)
