from polygon import RESTClient

# docs
# https://polygon.io/docs/crypto/get_v1_indicators_ema__cryptoticker
# https://github.com/polygon-io/client-python/blob/master/polygon/rest/indicators.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

ema = client.get_ema(
    ticker="X:BTCUSD",
    timespan="day",
    window=50,
    series_type="close",
)

print(ema)
