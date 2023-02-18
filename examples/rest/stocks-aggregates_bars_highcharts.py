from polygon import RESTClient
from polygon.rest.models import (
    Agg,
)
import datetime
import http.server
import socketserver
import traceback
import json

PORT = 8888

# https://canvasjs.com/javascript-stockcharts/stockchart-date-time-axis/
# JavaScript StockChart with Date-Time Axis
html = """
<!DOCTYPE HTML>
<html>
<head>

<style>
#container {
  height: 750px;
  min-width: 310px;
}
</style>

<script src="https://code.highcharts.com/stock/highstock.js"></script>
<script src="https://code.highcharts.com/stock/modules/data.js"></script>
<script src="https://code.highcharts.com/stock/modules/exporting.js"></script>
<script src="https://code.highcharts.com/stock/modules/accessibility.js"></script>

<div id="container"></div>

<script type="text/javascript">
Highcharts.getJSON('/data', function (data) {

  // create the chart
  Highcharts.stockChart('container', {
    rangeSelector: {
      selected: 1
    },

    title: {
      text: 'Stock Price'
    },

    series: [{
      type: 'candlestick',
      name: 'Stock Price',
      data: data
    }]
  });
});
</script>
</head>
<body>
"""

client = RESTClient()  # POLYGON_API_KEY environment variable is used

aggs = client.get_aggs(
    "AAPL",
    1,
    "day",
    "2019-01-01",
    "2023-02-16",
    limit=50000,
)

# print(aggs)

data = []

# writing data
for agg in aggs:

    # verify this is an agg
    if isinstance(agg, Agg):

        # verify this is an int
        if isinstance(agg.timestamp, int):

            new_record = {
                "date": agg.timestamp,
                "open": agg.open,
                "high": agg.high,
                "low": agg.low,
                "close": agg.close,
                "volume": agg.volume,
            }

            data.append(new_record)

values = [[v for k, v in d.items()] for d in data]

# json_data = json.dumps(data)
# print(json_data)


class handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        if self.path == "/data":
            self.send_response(200)
            self.send_header("Content-type", "application/json")
            self.end_headers()
            json_data = json.dumps(values)
            self.wfile.write(json_data.encode())
        else:
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            self.wfile.write(html.encode())


# handle ctrl-c KeyboardInterrupt to exit the program gracefully
try:
    while True:
        # run http server
        with socketserver.TCPServer(("", PORT), handler) as httpd:
            print("serving at port", PORT)
            httpd.serve_forever()
        pass
except KeyboardInterrupt:
    print("\nExiting gracefully...")
    # traceback.print_exc()
