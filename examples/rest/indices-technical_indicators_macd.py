from polygon import RESTClient

# docs
# https://polygon.io/docs/indices/get_v1_indicators_macd__indicesticker
# https://github.com/polygon-io/client-python/blob/master/polygon/rest/indicators.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

macd = client.get_macd("I:SPX")
print(macd)
