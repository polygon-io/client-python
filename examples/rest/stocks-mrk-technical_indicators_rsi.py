from polygon import RESTClient

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v1_indicators_rsi__stockticker
# https://github.com/polygon-io/client-python/blob/master/polygon/rest/indicators.py

rsi = client.get_rsi("AAPL")
print(rsi)
