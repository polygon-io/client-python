from polygon import RESTClient

c = RESTClient(api_key="API_KEY")

headers = {
    "X-Polygon-Edge-ID": "<EDGE_ID>",
    "X-Polygon-Edge-IP-Address": "<EDGE_IP_ADDRESS>",
    "X-Polygon-Edge-User-Agent": "<EDGE_USER_AGENT>",
}

res = c.get_ticker_events("META", headers=headers)

print(res)
