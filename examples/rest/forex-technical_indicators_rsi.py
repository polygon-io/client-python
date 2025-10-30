from massive import RESTClient

# docs
# https://massive.com/docs/forex/get_v1_indicators_rsi__fxticker
# https://github.com/massive-com/client-python/blob/master/massive/rest/indicators.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

rsi = client.get_rsi(
    ticker="C:EURUSD",
    timespan="day",
    window=14,
    series_type="close",
)

print(rsi)
