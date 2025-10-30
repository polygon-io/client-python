from massive import RESTClient

# docs
# https://massive.com/docs/forex/get_v1_marketstatus_now
# https://massive-api-client.readthedocs.io/en/latest/Reference.html#get-market-status

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

result = client.get_market_status()
print(result)
