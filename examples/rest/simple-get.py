from polygon import RESTClient
from polygon.rest import models

client = RESTClient()

options = models.required_edge_headers({}, "d", "b")
options = models.edge_user_agent(options, "user-agent")

aggs = client.get_aggs("AAPL", 1, "day", "2022-04-04", "2022-04-04", options=options)
print(aggs)
