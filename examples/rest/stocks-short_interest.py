from massive import RESTClient

# docs
# https://massive.com/docs/rest/stocks/fundamentals/short-interest

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

items = []
for item in client.list_short_interest(ticker="RDDT"):
    items.append(item)

print(items)
