from polygon import RESTClient

# docs
# https://polygon.io/docs/crypto/get_v3_reference_conditions
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#list-conditions

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

conditions = []
for c in client.list_conditions("crypto", limit=1000):
    conditions.append(c)
print(conditions)
