# LaunchPad

Users of the Launchpad product will need to pass in certain headers in order to make API requests.

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
from polygon.rest.models.request import RequestOptionBuilder

# create client
c = RESTClient(api_key="API_KEY")

# create request options
options = RequestOptionBuilder().required_edge_headers(
    edge_id="YOUR_EDGE_ID",  # required
    edge_ip_address="IP_ADDRESS"  # required
).optional_edge_headers(
    user_agent="USER_AGENT_ID"  # optional
)

# get response
res = c.get_ticker_events("META", options=options)

# do something with response

 ```