from polygon import RESTClient

# docs
# https://polygon.io/docs/stocks/get_vx_reference_financials
# https://polygon-api-client.readthedocs.io/en/latest/vX.html#list-stock-financials

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

financials = []
for f in client.vx.list_stock_financials("AAPL"):
    financials.append(f)
print(financials)
