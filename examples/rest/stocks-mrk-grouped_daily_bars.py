from polygon import RESTClient
import pprint

# client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX")  # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v2_aggs_grouped_locale_us_market_stocks__date
# https://polygon-api-client.readthedocs.io/en/latest/Aggs.html#get-grouped-daily-aggs

grouped = client.get_grouped_daily_aggs(
    "2023-02-07",
)

# print(grouped)

# pprint (short for "pretty-print") is a module that provides a more human-
# readable output format for data structures.
pp = pprint.PrettyPrinter(indent=2)
pp.pprint(grouped)
