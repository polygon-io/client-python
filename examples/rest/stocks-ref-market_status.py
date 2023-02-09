from polygon import RESTClient

#client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX") # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v1_marketstatus_now
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-market-status

result = client.get_market_status()
print(result)
