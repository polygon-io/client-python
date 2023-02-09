from polygon import RESTClient

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v3_reference_tickers
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#list-tickers

tickers = []
for t in client.list_tickers(limit=1000):
    tickers.append(t)
print(tickers)
