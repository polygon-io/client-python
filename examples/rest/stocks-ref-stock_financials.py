from polygon import RESTClient

#client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX") # api_key is used

# docs
# https://polygon.io/docs/stocks/get_vx_reference_financials
# https://polygon-api-client.readthedocs.io/en/latest/vX.html#list-stock-financials

financials = []
for f in client.vx.list_stock_financials("AAPL"):
    financials.append(f)
print(financials)