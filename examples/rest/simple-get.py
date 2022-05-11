from polygon import RESTClient

client = RESTClient(api_key="s7Cwsxiaj32BVtjrIvHkVwAiF9kytfyk")

aggs = client.get_aggs("AAPL", 1, "day", "2004-04-04", "2004-04-04")
print(aggs)
