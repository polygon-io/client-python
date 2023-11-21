from polygon import RESTClient

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

taxonomies = []
for t in client.vx.list_taxonomies(
    ticker_any_of=[
        "TSLA",
        "AAPL",
        "GME",
    ]
):
    taxonomies.append(t)

print(taxonomies)
