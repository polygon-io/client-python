from massive import RESTClient

# docs
# https://massive.com/docs/forex/get_v3_quotes__fxticker
# https://massive-api-client.readthedocs.io/en/latest/Quotes.html#list-quotes

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

quotes = []
for t in client.list_quotes("C:EUR-USD", "2023-02-01", limit=50000):
    quotes.append(t)
print(quotes)
