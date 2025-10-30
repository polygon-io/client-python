from massive import RESTClient
from massive.rest.models import (
    TickerNews,
)

# docs
# https://massive.com/docs/stocks/get_v2_reference_news
# https://massive-api-client.readthedocs.io/en/latest/Reference.html#list-ticker-news

# client = RESTClient("XXXXXX") # hardcoded api_key is used
client = RESTClient()  # MASSIVE_API_KEY environment variable is used

news = []
for n in client.list_ticker_news("BBBY", order="desc", limit=1000):
    news.append(n)

# print(news)

# print date + title
for index, item in enumerate(news):
    # verify this is an agg
    if isinstance(item, TickerNews):
        print("{:<25}{:<15}".format(item.published_utc, item.title))

        if index == 20:
            break
