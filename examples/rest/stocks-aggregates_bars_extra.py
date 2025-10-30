# This code retrieves stock market data for a specific stock using the
# Massive REST API and writes it to a CSV file. It uses the "massive"
# library to communicate with the API and the "csv" library to write
# the data to a CSV file. The script retrieves data for the stock "AAPL"
# for the dates "2023-01-30" to "2023-02-03" in 1 hour intervals. The
# resulting data includes the open, high, low, close, volume, vwap,
# timestamp, transactions, and otc values for each hour. The output is
# then printed to the console.
from massive import RESTClient
from massive.rest.models import (
    Agg,
)
import csv
import datetime
import io

# docs
# https://massive.com/docs/stocks/get_v2_aggs_ticker__stocksticker__range__multiplier___timespan___from___to
# https://massive-api-client.readthedocs.io/en/latest/Aggs.html#massive.RESTClient.list_aggs

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

aggs = []
for a in client.list_aggs(
    "AAPL",
    1,
    "hour",
    "2023-01-30",
    "2023-02-03",
    limit=50000,
):
    aggs.append(a)

print(aggs)

# headers
headers = [
    "timestamp",
    "open",
    "high",
    "low",
    "close",
    "volume",
    "vwap",
    "transactions",
    "otc",
]

# creating the csv string
csv_string = io.StringIO()
writer = csv.DictWriter(csv_string, fieldnames=headers)

# writing headers
writer.writeheader()

# writing data
for agg in aggs:
    # verify this is an agg
    if isinstance(agg, Agg):
        # verify this is an int
        if isinstance(agg.timestamp, int):
            writer.writerow(
                {
                    "timestamp": datetime.datetime.fromtimestamp(agg.timestamp / 1000),
                    "open": agg.open,
                    "high": agg.high,
                    "low": agg.low,
                    "close": agg.close,
                    "volume": agg.volume,
                    "vwap": agg.vwap,
                    "transactions": agg.transactions,
                    "otc": agg.otc,
                }
            )

# printing the csv string
print(csv_string.getvalue())
