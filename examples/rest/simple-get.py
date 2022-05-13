from polygon import RESTClient

client = RESTClient()

aggs = client.get_aggs("AAPL", 1, "day", "2022-04-04", "2022-04-04")
print(aggs)
