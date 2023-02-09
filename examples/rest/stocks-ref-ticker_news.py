from polygon import RESTClient

#client = RESTClient() # POLYGON_API_KEY is used
client = RESTClient("XXXXXX") # api_key is used

# docs
# https://polygon.io/docs/stocks/get_v2_reference_news
# https://polygon-api-client.readthedocs.io/en/latest/Reference.html#list-ticker-news

news = []
for n in client.list_ticker_news("BBBY", order="desc", limit=1000):
    news.append(n)

#print(news)

# print date + title
for index, item in enumerate(news):
    print("{:<25}{:<15}".format(item.published_utc, item.title))
    if index == 20:
        break
