from polygon import RESTClient

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v1_marketstatus_upcoming
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#get-market-holidays

holidays = client.get_market_holidays()
# print(holidays)

# print date, name, and exchange
for item in holidays:
    print("{:<15}{:<15}".format(item.date, item.name + " (" + item.exchange + ")"))
