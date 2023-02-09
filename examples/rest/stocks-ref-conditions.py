from polygon import RESTClient

#client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX") # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v3_reference_conditions
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#list-conditions

conditions = []
for c in client.list_conditions(limit=1000):
    conditions.append(c)
print(conditions)