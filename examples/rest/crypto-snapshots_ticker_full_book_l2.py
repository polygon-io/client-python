from polygon import RESTClient

# docs
# https://polygon.io/docs/crypto/get_v2_snapshot_locale_global_markets_crypto_tickers__ticker__book
# https://polygon-api-client.readthedocs.io/en/latest/Snapshot.html#get-crypto-l2-book-snapshot

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

snapshot = client.get_snapshot_crypto_book("X:BTCUSD")

# print raw values
print(snapshot)
