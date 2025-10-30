from massive import RESTClient

# docs
# https://massive.com/docs/crypto/get_v1_indicators_macd__cryptoticker
# https://github.com/massive-com/client-python/blob/master/massive/rest/indicators.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

macd = client.get_macd(
    ticker="X:BTCUSD",
    timespan="day",
    short_window=12,
    long_window=26,
    signal_window=9,
    series_type="close",
)

print(macd)
