from polygon import RESTClient

# docs
# https://polygon.io/docs/stocks/get_v1_related-companies__ticker

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

related_companies = client.get_related_companies("AAPL")
print(related_companies)
