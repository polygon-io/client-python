from polygon import RESTClient

client = RESTClient()

financials = client.get_ticker_details("NFLX")
print(financials)
