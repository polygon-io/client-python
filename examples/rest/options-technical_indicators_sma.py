from massive import RESTClient

# docs
# https://massive.com/docs/options/get_v1_indicators_sma__optionsticker
# https://github.com/massive-com/client-python/blob/master/massive/rest/indicators.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

sma = client.get_sma(
    ticker="O:SPY241220P00720000", timespan="day", window=50, series_type="close"
)

print(sma)
