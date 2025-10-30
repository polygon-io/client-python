from massive import RESTClient

# docs
# https://massive.com/docs/rest/economy/treasury-yields

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

yields = []
for date in client.list_treasury_yields():
    yields.append(date)

print(yields)
