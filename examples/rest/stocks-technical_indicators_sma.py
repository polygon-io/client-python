from massive import RESTClient

# docs
# https://massive.com/docs/stocks/get_v1_indicators_sma__stockticker
# https://github.com/massive-com/client-python/blob/master/massive/rest/indicators.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

sma = client.get_sma(
    ticker="AAPL",
    timespan="day",
    window=50,
    series_type="close",
)

print(sma)
