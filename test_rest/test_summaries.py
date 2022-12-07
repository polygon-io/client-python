from polygon.rest.models import (
    SummaryResult,
    Branding,
    Session,
    Options
)
from base import BaseTest


class SummariesTest(BaseTest):
    def test_get_summaries(self):
        ticker_any_of = ['NCLH']
        summary_results = self.c.get_summaries(ticker_any_of)
        expected = [
            SummaryResult(
                price=22.3,
                name="Norwegian Cruise Lines",
                ticker="NCLH",
                branding=Branding(
                    icon_url="https://api.polygon.io/icon.png",
                    logo_url="https://api.polygon.io/logo.svg",
                ),
                market_status="closed",
                type="stocks",
                session=Session(
                    change=-1.05,
                    change_percent=-4.67,
                    close=21.4,
                    early_trading_change=-0.39,
                    early_trading_change_percent=-0.07,
                    high=22.49,
                    late_trading_change=1.2,
                    late_trading_change_percent=3.92,
                    low=21.35,
                    open=22.49,
                    previous_close=22.45,
                    volume=37
                ),
            )
        ]
        self.assertEqual(summary_results, expected)
