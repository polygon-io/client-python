from polygon import RESTClient

# docs
# https://polygon.io/docs/rest/stocks/fundamentals/short-volume

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

items = []
for item in client.list_short_volume(ticker="RDDT"):
    items.append(item)

print(items)
