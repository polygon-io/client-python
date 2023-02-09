from polygon import RESTClient

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v1_indicators_ema__stockticker
# https://github.com/polygon-io/client-python/blob/master/polygon/rest/indicators.py

ema = client.get_ema("AAPL")
print(ema)
