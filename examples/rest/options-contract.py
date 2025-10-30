from massive import RESTClient

# docs
# https://massive.com/docs/options/get_v3_reference_options_contracts__options_ticker
# https://massive-api-client.readthedocs.io/en/latest/Contracts.html

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

contract = client.get_options_contract("O:EVRI240119C00002500")

# print raw values
print(contract)
