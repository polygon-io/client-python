from polygon import RESTClient

#client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX") # api_key is used

# docs
# https://polygon.io/docs/stocks/get_vx_reference_tickers__id__events
# https://github.com/polygon-io/client-python/blob/master/polygon/rest/reference.py

events = client.get_ticker_events("META")
print(events)