from massive import RESTClient

# docs
# https://massive.com/docs/stocks/get_v3_reference_dividends
# https://massive-api-client.readthedocs.io/en/latest/Reference.html#list-dividends

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

dividends = []
for d in client.list_dividends("MSFT", limit=1000):
    dividends.append(d)
print(dividends)
