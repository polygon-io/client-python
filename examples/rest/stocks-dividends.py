from polygon import RESTClient

# docs
# https://polygon.io/docs/stocks/get_v3_reference_dividends
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#list-dividends

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

dividends = []
for d in client.list_dividends("MSFT", limit=1000):
    dividends.append(d)
print(dividends)
