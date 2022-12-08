# Launchpad

Users of the Launchpad product will need to pass in certain headers in order to make API requests.

 ```python

# import RESTClient
from polygon import RESTClient
from polygon.rest.models.request import RequestOptionBuilder

# create client
c = RESTClient(api_key="API_KEY")

# create request options
options = RequestOptionBuilder().edge_headers(
    edge_id="YOUR_EDGE_ID",  # required
    edge_ip_address="IP_ADDRESS",  # required
)
# get response
res = c.get_aggs("AAPL", 1, "day", "2022-04-04", "2022-04-04", options=options)

# do something with response

 ```
Launchpad users can also provide the optional User Agent value describing their Edge User's origination request.

 ```python

# import RESTClient
from polygon import RESTClient
from polygon.rest.models.request import RequestOptionBuilder

# create client
c = RESTClient(api_key="API_KEY")

# create request options
options = RequestOptionBuilder().edge_headers(
    edge_id="YOUR_EDGE_ID",  # required
    edge_ip_address="IP_ADDRESS"  # required
).update_edge_header(
    edge_user="EDGE_USER" # optional
                     )

# get response
res = c.get_aggs("AAPL", 1, "day", "2022-04-04", "2022-04-04", options=options)

# do something with response

 ```