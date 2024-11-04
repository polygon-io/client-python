import os
import pickle
import json
from datetime import datetime
from polygon import RESTClient
from polygon.rest.models import Agg
import http.server
import socketserver
import traceback
from urllib.parse import urlparse, parse_qs

PORT = 8888

# Load the lookup_table
with open('lookup_table.pkl', 'rb') as f:
    lookup_table = pickle.load(f)

class handler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        # Parse the path and query parameters
        parsed_path = urlparse(self.path)
        path = parsed_path.path
        query_params = parse_qs(parsed_path.query)
        
        if path == '/':
            # Handle the root path
            # Get the date parameter if provided
            date_param = query_params.get('date', [None])[0]
            
            # Get all dates from the lookup table
            all_dates = set()
            for ticker_data in lookup_table.values():
                all_dates.update(ticker_data.keys())
            all_dates = sorted(all_dates)
            
            # If date is None, get the latest date from the lookup table
            if date_param is None:
                if all_dates:
                    latest_date = max(all_dates)
                else:
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    html_content = '<html><body><h1>No data available.</h1></body></html>'
                    self.wfile.write(html_content.encode())
                    return
            else:
                latest_date = date_param
            
            # Ensure latest_date is in all_dates
            if latest_date not in all_dates:
                # Handle the case where the provided date is invalid
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                error_html = f'<html><body><h1>Error: No data available for date {latest_date}</h1></body></html>'
                self.wfile.write(error_html.encode())
                return
            
            # Now, get the anomalies for the latest_date
            anomalies = []
            for ticker, date_data in lookup_table.items():
                if latest_date in date_data:
                    data = date_data[latest_date]
                    trades = data['trades']
                    avg_trades = data['avg_trades']
                    std_trades = data['std_trades']
                    if (
                        avg_trades is not None and
                        std_trades is not None and
                        std_trades > 0
                    ):
                        z_score = (trades - avg_trades) / std_trades
                        threshold_multiplier = 3  # Adjust as needed
                        if z_score > threshold_multiplier:
                            anomalies.append({
                                'ticker': ticker,
                                'date': latest_date,
                                'trades': trades,
                                'avg_trades': avg_trades,
                                'std_trades': std_trades,
                                'z_score': z_score,
                                'close_price': data['close_price'],
                                'price_diff': data['price_diff']
                            })
            # Sort anomalies by trades in descending order
            anomalies.sort(key=lambda x: x['trades'], reverse=True)
            # Generate the HTML to display the anomalies
            self.send_response(200)
            self.send_header("Content-type", "text/html")
            self.end_headers()
            # Build the HTML content
            html_content = '<html><link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous"><script src="https://cdnjs.cloudflare.com/ajax/libs/tablesort/5.2.1/tablesort.min.js" integrity="sha512-F/gIMdDfda6OD2rnzt/Iyp2V9JLHlFQ+EUyixDg9+rkwjqgW1snpkpx7FD5FV1+gG2fmFj7I3r6ReQDUidHelA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script><script src="https://cdnjs.cloudflare.com/ajax/libs/tablesort/5.2.1/sorts/tablesort.number.min.js" integrity="sha512-dRD755QRxlybm0h3LXXIGrFcjNakuxW3reZqnPtUkMv6YsSWoJf+slPjY5v4lZvx2ss+wBZQFegepmA7a2W9eA==" crossorigin="anonymous" referrerpolicy="no-referrer"></script><head><title>Anomalies for {}</title></head><body>'.format(latest_date)
            html_content += '<div id="container" style="padding:4px;"><h1>Anomalies for {}</h1>'.format(latest_date)
            # Add navigation links (prev and next dates)
            current_index = all_dates.index(latest_date)
            prev_date = all_dates[current_index - 1] if current_index > 0 else None
            next_date = all_dates[current_index + 1] if current_index < len(all_dates) - 1 else None
            html_content += '<p>'
            if prev_date:
                html_content += '<a href="/?date={}">Previous Date</a> '.format(prev_date)
            if next_date:
                html_content += '<a href="/?date={}">Next Date</a> '.format(next_date)
            html_content += '</p>'
            # Display the anomalies in a table
            html_content += '<table id="anomalies" class="table table-striped table-hover">'
            html_content += '<thead><tr>'
            html_content += '<th>Ticker</th>'
            html_content += '<th>Trades</th>'
            html_content += '<th>Avg Trades</th>'
            html_content += '<th>Std Dev</th>'
            html_content += '<th>Z-score</th>'
            html_content += '<th>Close Price</th>'
            html_content += '<th>Price Diff</th>'
            html_content += '<th>Chart</th>'
            html_content += '</tr></thead><tbody>'
            for anomaly in anomalies:
                html_content += '<tr>'
                html_content += '<td>{}</td>'.format(anomaly['ticker'])
                html_content += '<td>{}</td>'.format(anomaly['trades'])
                html_content += '<td>{:.2f}</td>'.format(anomaly['avg_trades'])
                html_content += '<td>{:.2f}</td>'.format(anomaly['std_trades'])
                html_content += '<td>{:.2f}</td>'.format(anomaly['z_score'])
                html_content += '<td>{:.2f}</td>'.format(anomaly['close_price'])
                html_content += '<td>{:.2f}</td>'.format(anomaly['price_diff'])
                # Add a link to the chart
                html_content += '<td><a href="/chart?ticker={}&date={}">View Chart</a></td>'.format(anomaly['ticker'], latest_date)
                html_content += '</tr>'
            html_content += '</tbody></table><script>new Tablesort(document.getElementById("anomalies"));</script>'
            html_content += '</div></body></html>'
            self.wfile.write(html_content.encode())
        elif path == '/chart':
            # Handle the chart page
            # Get 'ticker' and 'date' from query parameters
            ticker = query_params.get('ticker', [None])[0]
            date = query_params.get('date', [None])[0]
            if ticker is None or date is None:
                # Return an error page
                self.send_response(400)
                self.send_header("Content-type", "text/html")
                self.end_headers()
                error_html = '<html><body><h1>Error: Missing ticker or date parameter</h1></body></html>'
                self.wfile.write(error_html.encode())
            else:
                # Fetch minute aggregates for the ticker and date
                client = RESTClient(trace=True)  # POLYGON_API_KEY environment variable is used
                try:
                    aggs = []
                    date_from = date
                    date_to = date
                    for a in client.list_aggs(
                        ticker,
                        1,
                        "minute",
                        date_from,
                        date_to,
                        limit=50000,
                    ):
                        aggs.append(a)
                    # Prepare data for the chart
                    data = []
                    for agg in aggs:
                        if isinstance(agg, Agg) and isinstance(agg.timestamp, int):
                            new_record = [
                                agg.timestamp,
                                agg.open,
                                agg.high,
                                agg.low,
                                agg.close
                            ]
                            data.append(new_record)
                    # Generate the HTML for the chart page
                    chart_html = """
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
                    <script src="https://code.highcharts.com/moment/moment.js"></script>
                    <script src="https://code.highcharts.com/moment-timezone/moment-timezone.js"></script>
                    </head>
                    <body>
                    <div id="container">
                    <script type="text/javascript">
					Highcharts.setOptions({
					    global: {
					        timezone: 'America/New_York'
					    }
					});
                    var data = %s;
                    Highcharts.stockChart('container', {
				        exporting: {
				            url: 'http://localhost:7801', // Set your local server as the exporting server
				            enabled: true // Make sure exporting is enabled
				        },
					    rangeSelector: {
					        enabled: false,
					        selected: 1
					    },
					    navigator: {
					        //enabled: false
					    },
					    scrollbar: {
					        //enabled: false
					    },
					    xAxis: {
					        labels: {
					            //enabled: true // This hides the time labels under the chart
					        }
					    },
                        title: {
                          text: '%s Price Data on %s'
                        },
                        series: [{
                          type: 'candlestick',
                          name: '%s',
                          data: data,
                          color: 'red', // Color for downward movement
                          lineColor: 'red', // Line color for downward movement
                          upColor: 'green', // Color for upward movement
                          upLineColor: 'green', // Line color for upward movement
                          dataGrouping: {
                            units: [[
                              'minute',
                              [1]
                            ]]
                          }
                        }]
                      });
                    </script>
                    </div>
                    </body>
                    </html>
                    """ % (json.dumps(data), ticker, date, ticker)
                    self.send_response(200)
                    self.send_header("Content-type", "text/html")
                    self.send_header('Access-Control-Allow-Origin', '*')
                    self.end_headers()
                    self.wfile.write(chart_html.encode())
                except Exception as e:
                    # Handle exceptions
                    self.send_response(500)
                    self.send_header("Content-type", "text/html")
                    self.end_headers()
                    error_html = '<html><body><h1>Error fetching data: {}</h1></body></html>'.format(str(e))
                    self.wfile.write(error_html.encode())
        else:
            # Serve files from the current directory
            super().do_GET()

def run_server():
    with socketserver.TCPServer(("", PORT), handler) as httpd:
        print("serving at port", PORT)
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            print("\nExiting gracefully...")
            httpd.shutdown()
            httpd.server_close()

if __name__ == '__main__':
    run_server()
