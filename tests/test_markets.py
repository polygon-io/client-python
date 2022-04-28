from polygon import RESTClient
from polygon.rest.models import (
    MarketHoliday,
    MarketStatus
)
from mocks import BaseTest

class MarketsTest(BaseTest):
    def test_get_market_holidays(self):
        holidays = self.c.get_market_holidays()
        expected = [
            # MarketHoliday()
        ]
        self.assertEqual(holidays, expected)