from massive import RESTClient

# docs
# https://massive.com/docs/options/get_v3_reference_options_contracts
# https://massive-api-client.readthedocs.io/en/latest/Contracts.html#list-options-contracts

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

contracts = []
for c in client.list_options_contracts("HCP"):
    contracts.append(c)
print(contracts)
