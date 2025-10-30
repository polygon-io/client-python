from massive import RESTClient

# docs
# https://massive.com/docs/stocks/get_v2_aggs_ticker__stocksticker__range__multiplier___timespan___from___to
# https://massive-api-client.readthedocs.io/en/latest/Aggs.html#massive.RESTClient.list_aggs

client = RESTClient()  # MASSIVE_API_KEY environment variable is used

aggs = []
for a in client.list_aggs(
    "AAPL",
    1,
    "hour",
    "2024-01-30",
    "2024-01-30",
    limit=50000,
):
    aggs.append(a)

print(aggs)
