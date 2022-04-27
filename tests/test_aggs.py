from polygon import RESTClient
from polygon.rest.models import Agg
from mocks import BaseTest


class AggsTest(BaseTest):
    def test_get_aggs(self):
        c = RESTClient("")
        aggs = c.get_aggs("AAPL", 1, "day", "2005-04-01", "2005-04-04")
        expected = [
            Agg(
                open=1.5032,
                high=1.5064,
                low=1.4489,
                close=1.4604,
                volume=642646396.0,
                vwap=1.469,
                timestamp=1112331600000,
                transactions=82132,
            ),
            Agg(
                open=1.4639,
                high=1.4754,
                low=1.4343,
                close=1.4675,
                volume=578172308.0,
                vwap=1.4589,
                timestamp=1112587200000,
                transactions=65543,
            ),
        ]
        self.assertEqual(aggs, expected)
