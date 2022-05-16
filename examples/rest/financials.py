from polygon import RESTClient

client = RESTClient()

financials = client.get_ticker_details("NFLX")
print(financials)

for (i, n) in enumerate(client.list_ticker_news("INTC", limit=5)):
    print(i, n.description)
    if i == 5:
        break
