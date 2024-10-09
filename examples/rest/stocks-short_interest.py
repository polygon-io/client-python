from polygon import RESTClient

# docs
# https://polygon.io/docs/stocks/get_v1_reference_short-interest__identifierType___identifier

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

short_interest = []
for si in client.list_short_interest(
	identifier="AMD",
    identifier_type="ticker",
    params={
        "date.gte": "2024-10-07",
        "date.lte": "2024-10-07",
    },
    limit=100
):
    short_interest.append(si)

print(short_interest)
