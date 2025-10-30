from massive import RESTClient

# docs
# https://massive.com/docs/options/get_v1_indicators_macd__optionsticker
# https://github.com/massive-com/client-python/blob/master/massive/rest/indicators.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

macd = client.get_macd(
    ticker="O:SPY241220P00720000",
    timespan="day",
    short_window=12,
    long_window=26,
    signal_window=9,
    series_type="close",
)

print(macd)
