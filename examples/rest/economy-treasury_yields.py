from polygon import RESTClient

# docs
# https://polygon.io/docs/rest/economy/treasury-yields

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

yields = []
for date in client.vx.list_treasury_yields():
    yields.append(date)

print(yields)
