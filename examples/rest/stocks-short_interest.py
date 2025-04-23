from polygon import RESTClient

# docs
# https://polygon.io/docs/rest/stocks/fundamentals/short-interest

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

items = []
for item in client.vx.list_short_interest(ticker="RDDT"):
    items.append(item)

print(items)
