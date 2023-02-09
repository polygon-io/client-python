# This code retrieves trade records and counts the amount of money that changes hands.
from polygon import RESTClient

#client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX") # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v3_trades__stockticker
# https://polygon-api-client.readthedocs.io/en/latest/Trades.html#polygon.RESTClient.list_trades

# used to track money across trades
money = 0

# loop through and count price * volume
for t in client.list_trades("DIS", "2023-02-07", limit=50000):
    money += t.price * t.size

# format the number so it's human readable
formatted_number = "{:,.2f}".format(money)
print("Roughly " + formatted_number + " changed hands for DIS on 2023-02-07.")