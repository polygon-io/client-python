from polygon import RESTClient

#client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX") # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v3_quotes__stockticker
# https://polygon-api-client.readthedocs.io/en/latest/Quotes.html#list-quotes

# NBBO (National Best Bid and Offer) is a term used in the financial industry 
# to describe the best bid and offer prices for a particular stock or security
# being traded on all the available stock exchanges in the United States. It 
# provides information on the highest price a buyer is willing to pay (best 
# bid) and the lowest price a seller is willing to accept (best offer) for a 
# particular security. This information is used by traders to make informed 
# investment decisions and execute trades at the best available price.

quotes = []
for t in client.list_quotes("IBIO", "2023-02-01", limit=50000):
    quotes.append(t)
print(quotes)
