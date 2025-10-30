from massive import RESTClient

# docs
# https://massive.com/docs/crypto/get_v2_snapshot_locale_global_markets_crypto_tickers__ticker
# https://massive-api-client.readthedocs.io/en/latest/Snapshot.html#get-ticker-snapshot

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

ticker = client.get_snapshot_ticker("crypto", "X:BTCUSD")
print(ticker)
