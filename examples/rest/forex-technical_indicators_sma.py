from polygon import RESTClient

# docs
# https://polygon.io/docs/forex/get_v1_indicators_sma__fxticker
# https://github.com/polygon-io/client-python/blob/master/polygon/rest/indicators.py

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

sma = client.get_sma("C:EURUSD")
print(sma)
