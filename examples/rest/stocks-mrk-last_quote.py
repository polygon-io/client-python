from polygon import RESTClient

#client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX") # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v2_last_nbbo__stocksticker
# https://polygon-api-client.readthedocs.io/en/latest/Quotes.html#get-last-quote

quote = client.get_last_quote(
    "AAPL",
)

print(quote)
