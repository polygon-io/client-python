from polygon import RESTClient

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v3_reference_exchanges
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-exchanges

exchanges = client.get_exchanges()
# print(exchanges)

# print date, name, and exchange
for item in exchanges:
    print(
        "{:<15}{:<15}".format(
            item.asset_class, item.name + " (" + str(item.operating_mic) + ")"
        )
    )
