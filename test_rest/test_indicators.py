from base import BaseTest
from polygon.rest.models.aggs import Agg
from polygon.rest.models.indicators import SingleIndicatorResults, MACDIndicatorResults, IndicatorValue, MACDIndicatorValue, Underlying


class IndicatorsTest(BaseTest):
    def test_get_sma_indicators(self):
        indicators = self.c.get_indicators_sma("AAPL", 1, "day", "2005-04-01", "2005-04-04")
        expected = (
            SingleIndicatorResults(
                values=[
                    IndicatorValue(
                        Timestamp=12324,
                        Value=43.3
                    ),
                    IndicatorValue(
                        Timestamp=12324,
                        Value=43.3
                    ),
                ],
                underlying=Underlying(
                    url="url",
                    aggregates=[
                        Agg(),
                        Agg(),
                    ],
                )
            )
        )
        self.assertEqual(indicators, expected)
