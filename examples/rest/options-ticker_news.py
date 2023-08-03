from polygon import RESTClient
from polygon.rest.models import (
    TickerNews,
)

# docs
# https://polygon.io/docs/options/get_v2_reference_news
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#list-ticker-news

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # POLYGON_API_KEY environment variable is used

news = []
for n in client.list_ticker_news("AAPL", order="desc", limit=1000):
    news.append(n)

# print date + title
for index, item in enumerate(news):
    # verify this is an agg
    if isinstance(item, TickerNews):
        print("{:<25}{:<15}".format(item.published_utc, item.title))

        if index == 20:
            break
