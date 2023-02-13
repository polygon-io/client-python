from polygon import RESTClient

# docs
# https://polygon.io/docs/stocks/get_v1_marketstatus_now
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-market-status

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

result = client.get_market_status()
print(result)
