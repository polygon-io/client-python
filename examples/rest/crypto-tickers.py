from massive import RESTClient

# docs
# https://massive.com/docs/crypto/get_v3_reference_tickers
# https://massive-api-client.readthedocs.io/en/latest/Reference.html#list-tickers

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

tickers = []
for t in client.list_tickers(market="crypto", limit=1000):
    tickers.append(t)
print(tickers)
