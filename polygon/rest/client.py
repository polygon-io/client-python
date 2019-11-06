from typing import Dict

import requests

from polygon.rest import models
from polygon.rest.models import unmarshal


class RESTClient:
    """ This is a custom generated class """
    DEFAULT_HOST = "api.polygon.io"

    def __init__(self, auth_key: str):
        self.auth_key = auth_key
        self.url = "https://" + self.DEFAULT_HOST

        self._session = requests.Session()
        self._session.params["apiKey"] = self.auth_key

    def _handle_response(self, response_type: str, endpoint: str, params: Dict[str, str]) -> models.Definition:
        resp: requests.Response = self._session.get(endpoint, params=params)
        if resp.status_code == 200:
            return unmarshal.unmarshal_json(response_type, resp.json())
        else:
            resp.raise_for_status()

    def tickers(self, **query_params):
        endpoint = f"{self.url}/v2/reference/tickers"
        return self._handle_response("TickersApiResponse", endpoint, query_params)

    def ticker_types(self, **query_params):
        endpoint = f"{self.url}/v2/reference/types"
        return self._handle_response("TickerTypesApiResponse", endpoint, query_params)

    def ticker_details(self, symbol, **query_params):
        endpoint = f"{self.url}/v1/meta/symbols/{symbol}/company"
        return self._handle_response("TickerDetailsApiResponse", endpoint, query_params)

    def ticker_news(self, symbol, **query_params):
        endpoint = f"{self.url}/v1/meta/symbols/{symbol}/news"
        return self._handle_response("TickerNewsApiResponse", endpoint, query_params)

    def markets(self, **query_params):
        endpoint = f"{self.url}/v2/reference/markets"
        return self._handle_response("MarketsApiResponse", endpoint, query_params)

    def locales(self, **query_params):
        endpoint = f"{self.url}/v2/reference/locales"
        return self._handle_response("LocalesApiResponse", endpoint, query_params)

    def stock_splits(self, symbol, **query_params):
        endpoint = f"{self.url}/v2/reference/splits/{symbol}"
        return self._handle_response("StockSplitsApiResponse", endpoint, query_params)

    def stock_dividends(self, symbol, **query_params):
        endpoint = f"{self.url}/v2/reference/dividends/{symbol}"
        return self._handle_response("StockDividendsApiResponse", endpoint, query_params)

    def stock_financials(self, symbol, **query_params):
        endpoint = f"{self.url}/v2/reference/financials/{symbol}"
        return self._handle_response("StockFinancialsApiResponse", endpoint, query_params)

    def market_status(self, **query_params):
        endpoint = f"{self.url}/v1/marketstatus/now"
        return self._handle_response("MarketStatusApiResponse", endpoint, query_params)

    def market_holidays(self, **query_params):
        endpoint = f"{self.url}/v1/marketstatus/upcoming"
        return self._handle_response("MarketHolidaysApiResponse", endpoint, query_params)

    def exchanges(self, **query_params):
        endpoint = f"{self.url}/v1/meta/exchanges"
        return self._handle_response("ExchangesApiResponse", endpoint, query_params)

    def historic_trades(self, symbol, date, **query_params):
        endpoint = f"{self.url}/v1/historic/trades/{symbol}/{date}"
        return self._handle_response("HistoricTradesApiResponse", endpoint, query_params)

    def historic_trades_v2(self, ticker, date, **query_params):
        endpoint = f"{self.url}/v2/ticks/stocks/trades/{ticker}/{date}"
        return self._handle_response("HistoricTradesV2ApiResponse", endpoint, query_params)

    def historic_quotes(self, symbol, date, **query_params):
        endpoint = f"{self.url}/v1/historic/quotes/{symbol}/{date}"
        return self._handle_response("HistoricQuotesApiResponse", endpoint, query_params)

    def historic_n___bbo_quotes_v2(self, ticker, date, **query_params):
        endpoint = f"{self.url}/v2/ticks/stocks/nbbo/{ticker}/{date}"
        return self._handle_response("HistoricNBboQuotesV2ApiResponse", endpoint, query_params)

    def last_trade_for_a_symbol(self, symbol, **query_params):
        endpoint = f"{self.url}/v1/last/stocks/{symbol}"
        return self._handle_response("LastTradeForASymbolApiResponse", endpoint, query_params)

    def last_quote_for_a_symbol(self, symbol, **query_params):
        endpoint = f"{self.url}/v1/last_quote/stocks/{symbol}"
        return self._handle_response("LastQuoteForASymbolApiResponse", endpoint, query_params)

    def daily_open_close(self, symbol, date, **query_params):
        endpoint = f"{self.url}/v1/open-close/{symbol}/{date}"
        return self._handle_response("DailyOpenCloseApiResponse", endpoint, query_params)

    def condition_mappings(self, ticktype, **query_params):
        endpoint = f"{self.url}/v1/meta/conditions/{ticktype}"
        return self._handle_response("ConditionMappingsApiResponse", endpoint, query_params)

    def snapshot_all_tickers(self, **query_params):
        endpoint = f"{self.url}/v2/snapshot/locale/us/markets/stocks/tickers"
        return self._handle_response("SnapshotAllTickersApiResponse", endpoint, query_params)

    def snapshot_single_ticker(self, ticker, **query_params):
        endpoint = f"{self.url}/v2/snapshot/locale/us/markets/stocks/tickers/{ticker}"
        return self._handle_response("SnapshotSingleTickerApiResponse", endpoint, query_params)

    def snapshot_gainers_losers(self, direction, **query_params):
        endpoint = f"{self.url}/v2/snapshot/locale/us/markets/stocks/{direction}"
        return self._handle_response("SnapshotGainersLosersApiResponse", endpoint, query_params)

    def previous_close(self, ticker, **query_params):
        endpoint = f"{self.url}/v2/aggs/ticker/{ticker}/prev"
        return self._handle_response("PreviousCloseApiResponse", endpoint, query_params)

    def aggregates(self, ticker, multiplier, timespan, from_, to, **query_params):
        endpoint = f"{self.url}/v2/aggs/ticker/{ticker}/range/{multiplier}/{timespan}/{from_}/{to}"
        return self._handle_response("AggregatesApiResponse", endpoint, query_params)

    def grouped_daily(self, locale, market, date, **query_params):
        endpoint = f"{self.url}/v2/aggs/grouped/locale/{locale}/market/{market}/{date}"
        return self._handle_response("GroupedDailyApiResponse", endpoint, query_params)

    def historic_forex_ticks(self, from_, to, date, **query_params):
        endpoint = f"{self.url}/v1/historic/forex/{from_}/{to}/{date}"
        return self._handle_response("HistoricForexTicksApiResponse", endpoint, query_params)

    def real_time_currency_conversion(self, from_, to, **query_params):
        endpoint = f"{self.url}/v1/conversion/{from_}/{to}"
        return self._handle_response("RealTimeCurrencyConversionApiResponse", endpoint, query_params)

    def last_quote_for_a_currency_pair(self, from_, to, **query_params):
        endpoint = f"{self.url}/v1/last_quote/currencies/{from_}/{to}"
        return self._handle_response("LastQuoteForACurrencyPairApiResponse", endpoint, query_params)

    def snapshot_all_tickers(self, **query_params):
        endpoint = f"{self.url}/v2/snapshot/locale/global/markets/forex/tickers"
        return self._handle_response("SnapshotAllTickersApiResponse", endpoint, query_params)

    def snapshot_gainers_losers(self, direction, **query_params):
        endpoint = f"{self.url}/v2/snapshot/locale/global/markets/forex/{direction}"
        return self._handle_response("SnapshotGainersLosersApiResponse", endpoint, query_params)

    def crypto_exchanges(self, **query_params):
        endpoint = f"{self.url}/v1/meta/crypto-exchanges"
        return self._handle_response("CryptoExchangesApiResponse", endpoint, query_params)

    def last_trade_for_a_crypto_pair(self, from_, to, **query_params):
        endpoint = f"{self.url}/v1/last/crypto/{from_}/{to}"
        return self._handle_response("LastTradeForACryptoPairApiResponse", endpoint, query_params)

    def daily_open_close(self, from_, to, date, **query_params):
        endpoint = f"{self.url}/v1/open-close/crypto/{from_}/{to}/{date}"
        return self._handle_response("DailyOpenCloseApiResponse", endpoint, query_params)

    def historic_crypto_trades(self, from_, to, date, **query_params):
        endpoint = f"{self.url}/v1/historic/crypto/{from_}/{to}/{date}"
        return self._handle_response("HistoricCryptoTradesApiResponse", endpoint, query_params)

    def snapshot_all_tickers(self, **query_params):
        endpoint = f"{self.url}/v2/snapshot/locale/global/markets/crypto/tickers"
        return self._handle_response("SnapshotAllTickersApiResponse", endpoint, query_params)

    def snapshot_single_ticker(self, ticker, **query_params):
        endpoint = f"{self.url}/v2/snapshot/locale/global/markets/crypto/tickers/{ticker}"
        return self._handle_response("SnapshotSingleTickerApiResponse", endpoint, query_params)

    def snapshot_single_ticker_full_book(self, ticker, **query_params):
        endpoint = f"{self.url}/v2/snapshot/locale/global/markets/crypto/tickers/{ticker}/book"
        return self._handle_response("SnapshotSingleTickerFullBookApiResponse", endpoint, query_params)

    def snapshot_gainers_losers(self, direction, **query_params):
        endpoint = f"{self.url}/v2/snapshot/locale/global/markets/crypto/{direction}"
        return self._handle_response("SnapshotGainersLosersApiResponse", endpoint, query_params)
