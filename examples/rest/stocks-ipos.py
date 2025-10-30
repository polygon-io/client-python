from massive import RESTClient

# docs
# https://massive.com/docs/rest/stocks/corporate-actions/ipos

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

ipos = []
for ipo in client.vx.list_ipos(ticker="RDDT"):
    ipos.append(ipo)

print(ipos)
