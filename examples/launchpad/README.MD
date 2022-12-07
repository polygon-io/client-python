# Launchpad

### Enpoints Currently supporting Launchpad
```
Aggs:
def get_aggs()

Reference:
def list_tickers()
def get_ticker_details()
def get_ticker_events()
def list_ticker_news()
def get_ticker_types()
def list_options_contracts()
def get_options_contracts()
def get_exchanges()
def list_conditions()
def list_dividends()
def list_splits()


Snapshot:
def get_snapshot_all()
def get_snapshot_direction()
def get_snapshot_ticker()
def get_snapshot_option()
def get_snapshot_crypto_book()

VX:
def list_stock_financials()
```

## EdgeHeaders
EdgeHeaders can be passed into request calls, the additional parameter is available in all reference client functions,
get_aggs, and snapshots

###### X-Polygon-Edge-ID
...[DESCRIPTION PENDING]
###### X-Polygon-Edge-IP-Address
...[DESCRIPTION PENDING]
###### X-Polygon-Edge-User-Agent
...[DESCRIPTION PENDING]

## Example
```python
# import RESTClient
from polygon import RESTClient

# create client
c = RESTClient(api_key="API_KEY")

# create header dict
headers = {
    "X-Polygon-Edge-ID": "<EDGE_ID>",
    "X-Polygon-Edge-IP-Address": "<EDGE_IP_ADDRESS>",
    "X-Polygon-Edge-User-Agent": "<EDGE_USER_AGENT>"
}

# get response
res = c.get_ticker_events("META",headers=headers)

# do something with response.
```

