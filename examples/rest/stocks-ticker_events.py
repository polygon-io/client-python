from massive import RESTClient

# docs
# https://massive.com/docs/stocks/get_vx_reference_tickers__id__events
# https://github.com/massive-com/client-python/blob/master/massive/rest/reference.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

events = client.get_ticker_events("META")
print(events)
