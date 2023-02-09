from polygon import RESTClient

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v3_reference_dividends
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#list-dividends

dividends = []
for d in client.list_dividends("MSFT", limit=1000):
    dividends.append(d)
print(dividends)
