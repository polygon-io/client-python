from massive import RESTClient

# docs
# https://massive.com/docs/stocks/get_v3_reference_conditions
# https://massive-api-client.readthedocs.io/en/latest/Reference.html#list-conditions

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

conditions = []
for c in client.list_conditions(limit=1000):
    conditions.append(c)
print(conditions)
