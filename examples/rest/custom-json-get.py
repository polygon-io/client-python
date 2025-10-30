from massive import RESTClient

# type: ignore
import orjson

client = RESTClient(custom_json=orjson)

aggs = client.get_aggs("AAPL", 1, "day", "2022-04-04", "2022-04-04")
print(aggs)
