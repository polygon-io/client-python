from polygon import RESTClient
from polygon.rest.models import (
    Ticker,
    TickerDetails,
    TickerNews,
    TickerTypes,
)
from mocks import BaseTest


class TickersTest(BaseTest):
    def test_list_tickers(self):
        tickers = [t for t in self.c.list_tickers()]
        expected = [
            Ticker(
                active=True,
                cik=None,
                composite_figi="BBG00X5FSP48",
                currency_name="usd",
                currency_symbol=None,
                base_currency_symbol=None,
                base_currency_name=None,
                delisted_utc=None,
                last_updated_utc="2022-04-27T00:00:00Z",
                locale="us",
                market="stocks",
                name="AAF First Priority CLO Bond ETF",
                primary_exchange="ARCX",
                share_class_figi="BBG00X5FSPZ4",
                ticker="AAA",
                type="ETF",
            ),
            Ticker(
                active=True,
                cik="0001708646",
                composite_figi="BBG00LPXX872",
                currency_name="usd",
                currency_symbol=None,
                base_currency_symbol=None,
                base_currency_name=None,
                delisted_utc=None,
                last_updated_utc="2022-04-27T00:00:00Z",
                locale="us",
                market="stocks",
                name="Goldman Sachs Physical Gold ETF Shares",
                primary_exchange="BATS",
                share_class_figi="BBG00LPXX8Z1",
                ticker="AAAU",
                type="ETF",
            ),
        ]
        self.assertEqual(tickers, expected)
