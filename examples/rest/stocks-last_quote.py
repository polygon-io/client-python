from massive import RESTClient

# docs
# https://massive.com/docs/stocks/get_v2_last_nbbo__stocksticker
# https://massive-api-client.readthedocs.io/en/latest/Quotes.html#get-last-quote

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

quote = client.get_last_quote(
    "AAPL",
)

print(quote)
