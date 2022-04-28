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

    def test_get_ticker_details(self):
        details = self.c.get_ticker_details("AAPL")
        expected = [
            TickerDetails(
                active=True,
                address={
                    "address1": "ONE APPLE PARK WAY",
                    "city": "CUPERTINO",
                    "state": "CA",
                    "postal_code": "95014",
                },
                branding={
                    "logo_url": "https://api.polygon.io/v1/reference/company-branding/d3d3LmFwcGxlLmNvbQ/images/2022-02-01_logo.svg",
                    "icon_url": "https://api.polygon.io/v1/reference/company-branding/d3d3LmFwcGxlLmNvbQ/images/2022-02-01_icon.png",
                },
                cik="0000320193",
                composite_figi="BBG000B9XRY4",
                currency_name="usd",
                delisted_utc=None,
                description="Apple designs a wide variety of consumer electronic devices, including smartphones (iPhone), tablets (iPad), PCs (Mac), smartwatches (Apple Watch), AirPods, and TV boxes (Apple TV), among others. The iPhone makes up the majority of Apples total revenue. In addition, Apple offers its customers a variety of services such as Apple Music, iCloud, Apple Care, Apple TV+, Apple Arcade, Apple Card, and Apple Pay, among others. Apples products run internally developed software and semiconductors, and the firm is well known for its integration of hardware, software and services. Apples products are distributed online as well as through company-owned stores and third-party retailers. The company generates roughly 40% of its revenue from the Americas, with the remainder earned internationally.",
                ticker_root="AAPL",
                homepage_url="https://www.apple.com",
                list_date="1980-12-12",
                locale="us",
                market="stocks",
                market_cap=2671492491700.0,
                name="Apple Inc.",
                phone_number="(408) 996-1010",
                primary_exchange="XNAS",
                share_class_figi="BBG001S5N8V8",
                share_class_shares_outstanding=16319440000,
                sic_code="3571",
                sic_description="ELECTRONIC COMPUTERS",
                ticker="AAPL",
                total_employees=154000,
                type="CS",
                weighted_shares_outstanding=16319441000,
            )
        ]
        self.assertEqual(details, expected)
