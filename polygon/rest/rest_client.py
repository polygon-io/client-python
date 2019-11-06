import logging

import requests


class RESTClient:
    DEFAULT_HOST = "api.polygon.io"

    def __init__(self, auth_key: str, debug: bool = False):
        self.auth_key = auth_key
        self.url = "https://" + self.DEFAULT_HOST

        self._session = requests.Session()
        self._session.params["apiKey"] = self.auth_key

        logging.basicConfig(level=logging.DEBUG if debug else None)

    def tickers(self, **params):
        endpoint = f"{self.url}/v2/reference/tickers"
        return self._session.get(endpoint, params=params)

    def ticker_types(self, **params):
        endpoint = f"{self.url}/v2/references/types"
        return self._session.get(endpoint, params=params)

    def ticker_details(self, symbol, **params):
        endpoint = f"{self.url}/v1/meta/symbols/{symbol}/company"
        return self._session.get(endpoint, params=params)

    def ticker_news(self, symbol, **params):
        endpoint = f"{self.url}/v1/meta/symbols/{symbol}/news"
        return self._session.get(endpoint, params=params)