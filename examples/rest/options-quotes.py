from massive import RESTClient

# docs
# https://massive.com/docs/options/get_v3_quotes__optionsticker
# https://massive-api-client.readthedocs.io/en/latest/Quotes.html#list-quotes

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

quotes = []
for t in client.list_quotes("O:SPY241220P00720000", limit=50000):
    quotes.append(t)
print(quotes)
