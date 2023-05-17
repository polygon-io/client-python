# This code retrieves trade records and counts the amount of money that changes hands.
from polygon import RESTClient
from polygon.rest.models import (
    Trade,
)

# docs
# https://polygon.io/docs/stocks/get_v3_trades__stockticker
# https://polygon-api-client.readthedocs.io/en/latest/Trades.html#polygon.RESTClient.list_trades

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

# used to track money across trades
money = float(0)

# loop through and count price * volume
for t in client.list_trades("DIS", "2023-02-07", limit=50000):

    # verify this is an Trade
    if isinstance(t, Trade):

        # verify these are float
        if isinstance(t.price, float) and isinstance(t.size, int):

            money += t.price * t.size

# format the number so it's human readable
formatted_number = "{:,.2f}".format(money)
print("Roughly " + formatted_number + " changed hands for DIS on 2023-02-07.")
