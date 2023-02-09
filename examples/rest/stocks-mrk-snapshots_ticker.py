from polygon import RESTClient

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v2_snapshot_locale_us_markets_stocks_tickers__stocksticker
# https://polygon-api-client.readthedocs.io/en/latest/Snapshot.html#get-ticker-snapshot

ticker = client.get_snapshot_ticker("stocks", "AAPL")
print(ticker)
