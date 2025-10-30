from massive import RESTClient

# docs
# https://massive.com/docs/forex/get_v1_indicators_macd__fxticker
# https://github.com/massive-com/client-python/blob/master/massive/rest/indicators.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

macd = client.get_macd(
    ticker="C:EURUSD",
    timespan="day",
    short_window=12,
    long_window=26,
    signal_window=9,
    series_type="close",
)

print(macd)
