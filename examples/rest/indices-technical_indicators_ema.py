from massive import RESTClient

# docs
# https://massive.com/docs/indices/get_v1_indicators_ema__indicesticker
# https://github.com/massive-com/client-python/blob/master/massive/rest/indicators.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

ema = client.get_ema(
    ticker="I:SPX",
    timespan="day",
    window=50,
    series_type="close",
)

print(ema)
