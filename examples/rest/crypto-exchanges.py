from massive import RESTClient
from massive.rest.models import (
    Exchange,
)

# docs
# https://massive.com/docs/crypto/get_v3_reference_exchanges
# https://massive-api-client.readthedocs.io/en/latest/Reference.html#get-exchanges

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

exchanges = client.get_exchanges("crypto")
print(exchanges)

# loop over exchanges
for exchange in exchanges:
    # verify this is an exchange
    if isinstance(exchange, Exchange):
        # print exchange info
        print(
            "{:<15}{} ({})".format(
                exchange.asset_class, exchange.name, exchange.operating_mic
            )
        )
