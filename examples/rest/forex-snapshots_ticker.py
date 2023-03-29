from polygon import RESTClient

# docs
# https://polygon.io/docs/forex/get_v2_snapshot_locale_global_markets_forex_tickers__ticker
# https://polygon-api-client.readthedocs.io/en/latest/Snapshot.html#get-ticker-snapshot

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

ticker = client.get_snapshot_ticker("forex", "C:EURUSD")
print(ticker)
