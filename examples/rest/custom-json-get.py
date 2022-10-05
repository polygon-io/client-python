from polygon import RESTClient
from examples import custom_json

client = RESTClient(custom_json=custom_json)

aggs = client.get_aggs("AAPL", 1, "day", "2022-04-04", "2022-04-04")
print(aggs)
