# This code retrieves stock market data for a specific stock using the
# Polygon REST API and writes it to a CSV file. It uses the "polygon"
# library to communicate with the API and the "csv" library to write
# the data to a CSV file. The script retrieves data for the stock "AAPL"
# for the dates "2023-01-30" to "2023-02-03" in 1 hour intervals. The
# resulting data includes the open, high, low, close, volume, vwap,
# timestamp, transactions, and otc values for each hour. The output is
# then printed to the console.
from polygon import RESTClient
import csv
import datetime

# client = RESTClient() # POLYGON_API_KEY environment variable used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v2_aggs_ticker__stocksticker__range__multiplier___timespan___from___to
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#polygon.RESTClient.get_aggs

aggs = client.get_aggs(
    "AAPL",
    1,
    "hour",
    "2023-01-30",
    "2023-02-03",
)

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
csv_string = csv.StringIO()
writer = csv.DictWriter(csv_string, fieldnames=headers)

# writing headers
writer.writeheader()

# writing data
for d in aggs:
    writer.writerow(
        {
            "timestamp": datetime.datetime.fromtimestamp(d.timestamp / 1000),
            "open": d.open,
            "high": d.high,
            "low": d.low,
            "close": d.close,
            "volume": d.volume,
            "vwap": d.vwap,
            "transactions": d.transactions,
            "otc": d.otc,
        }
    )

# printing the csv string
print(csv_string.getvalue())
