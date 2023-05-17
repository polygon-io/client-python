from polygon import RESTClient

# docs
# https://polygon.io/docs/forex/get_v1_last_quote_currencies__from___to
# https://polygon-api-client.readthedocs.io/en/latest/Quotes.html#get-last-forex-quote

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

quote = client.get_last_forex_quote(
    "AUD",
    "USD",
)

print(quote)
