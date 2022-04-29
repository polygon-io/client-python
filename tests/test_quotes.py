from mocks import BaseTest
from polygon.rest.models import (
    Quote,
    LastQuote,
    LastQuoteCurrencyPair,
    RealTimeCurrencyConversion,
    LastQuoteCurrencyPairLast,
)


class QuotesTest(BaseTest):
    def test_list_quotes(self):
        quotes = [q for q in self.c.list_quotes("AAPL", limit=1)]
        expected = [
            Quote(
                ask_exchange=12,
                ask_price=159.66,
                ask_size=4,
                bid_exchange=12,
                bid_price=159.65,
                bid_size=3,
                conditions=None,
                indicators=None,
                participant_timestamp=1651258089126196693,
                sequence_number=85374772,
                sip_timestamp=1651258089126211647,
                tape=3,
                trf_timestamp=None,
            )
        ]
        self.assertEqual(quotes, expected)

    def test_get_last_quote(self):
        quote = self.c.get_last_quote("AAPL")
        expected = [
            LastQuote(
                ticker="AAPL",
                trf_timestamp=None,
                sequence_number=86710587,
                sip_timestamp=1651258489041139455,
                participant_timestamp=1651258489040965640,
                ask_price=159.51,
                ask_size=2,
                ask_exchange=12,
                conditions=None,
                indicators=None,
                bid_price=159.5,
                bid_size=16,
                bid_exchange=11,
                tape=3,
            )
        ]
        self.assertEqual(quote, expected)

    def test_get_last_quote_currency_pair(self):
        quote = self.c.get_last_quote_currency_pair("AUD", "USD")
        expected = [
            LastQuoteCurrencyPairLast(
                ask=0.7085, bid=0.7081, exchange=48, timestamp=1651258681000
            )
        ]
        self.assertEqual(quote, expected)

    def test_realtime_currency_conversion(self):
        quote = self.c.get_realtime_currency_conversion("AUD", "USD", amount=100)
        expected = RealTimeCurrencyConversion(
            last=LastQuoteCurrencyPairLast(
                ask=1.4116318, bid=1.4115123, exchange=48, timestamp=1651259043000
            ),
            request_id="fac0cbd15f33070754880ace220d12b9",
            status="success",
            ticker="USD/AUD",
            from_="AUD",
            to="USD",
            converted=70.85,
            initial_amount=100,
        )
        self.assertEqual(quote, expected)
