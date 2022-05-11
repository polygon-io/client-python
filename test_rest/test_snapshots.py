from polygon.rest.models import (
    TickerSnapshot,
    OptionContractSnapshot,
    SnapshotTickerFullBook,
    Agg,
    MinuteSnapshot,
    OrderBookQuote,
    UnderlyingAsset,
    LastQuoteOptionContractSnapshot,
    Greeks,
    OptionDetails,
    DayOptionContractSnapshot,
)
from base import BaseTest


class SnapshotsTest(BaseTest):
    def test_get_snapshot_all(self):
        snapshots = self.c.get_snapshot_all()
        expected = [
            TickerSnapshot(
                day=Agg(
                    open=20.64,
                    high=20.64,
                    low=20.506,
                    close=20.506,
                    volume=37216,
                    vwap=20.616,
                    timestamp=None,
                    transactions=None,
                ),
                last_quote=None,
                last_trade=None,
                min=MinuteSnapshot(
                    accumulated_volume=37216,
                    open=20.506,
                    high=20.506,
                    low=20.506,
                    close=20.506,
                    volume=5000,
                    vwap=20.5105,
                ),
                prev_day=None,
                ticker="BCAT",
                todays_change=None,
                todays_change_percent=None,
                updated=1605192894630916600,
            )
        ]
        self.assertEqual(snapshots, expected)

    def test_get_snapshot_ticker(self):
        snapshots = self.c.get_snapshot_ticker("AAPL")
        expected = TickerSnapshot(
            day=Agg(
                open=161.84,
                high=166.2,
                low=159.8,
                close=160.315,
                volume=68840127,
                vwap=162.7124,
                timestamp=None,
                transactions=None,
            ),
            last_quote=None,
            last_trade=None,
            min=MinuteSnapshot(
                accumulated_volume=68834255,
                open=160.71,
                high=160.71,
                low=160.3,
                close=160.3,
                volume=197226,
                vwap=160.5259,
            ),
            prev_day=None,
            ticker="AAPL",
            todays_change=None,
            todays_change_percent=None,
            updated=1651251948294080343,
        )
        self.assertEqual(snapshots, expected)

    def test_get_snapshot_option(self):
        snapshots = self.c.get_snapshot_option("AAPL", "O:AAPL230616C00150000")
        expected = OptionContractSnapshot(
            break_even_price=179.075,
            day=DayOptionContractSnapshot(
                change=-2.3999999999999986,
                change_percent=-7.643312101910824,
                close=29,
                high=32.25,
                last_updated=1651204800000000000,
                low=29,
                open=29.99,
                previous_close=31.4,
                volume=8,
                vwap=30.7738,
            ),
            details=OptionDetails(
                contract_type="call",
                exercise_style="american",
                expiration_date="2023-06-16",
                shares_per_contract=100,
                strike_price=150,
                ticker="O:AAPL230616C00150000",
            ),
            greeks=Greeks(
                delta=0.6436614934293701,
                gamma=0.0061735291012820675,
                theta=-0.028227189324641973,
                vega=0.6381159723175714,
            ),
            implied_volatility=0.3570277203465058,
            last_quote=LastQuoteOptionContractSnapshot(
                ask=29.25,
                ask_size=209,
                bid=28.9,
                bid_size=294,
                last_updated=1651254260800059648,
                midpoint=29.075,
                timeframe="REAL-TIME",
            ),
            open_interest=8133,
            underlying_asset=UnderlyingAsset(
                change_to_break_even=19.11439999999999,
                last_updated=1651254263172073152,
                price=159.9606,
                ticker="AAPL",
                timeframe="REAL-TIME",
            ),
        )
        self.assertEqual(snapshots, expected)

    def test_get_snapshot_crypto_book(self):
        snapshots = self.c.get_snapshot_crypto_book("X:BTCUSD")
        expected = SnapshotTickerFullBook(
            ticker="X:BTCUSD",
            bids=[
                OrderBookQuote(price=16303.17, exchange_shares={"1": 2}),
                OrderBookQuote(
                    price=16302.94, exchange_shares={"1": 0.02859424, "6": 0.023455}
                ),
            ],
            asks=[
                OrderBookQuote(price=11454, exchange_shares={"2": 1}),
                OrderBookQuote(price=11455, exchange_shares={"2": 1}),
            ],
            bid_count=None,
            ask_count=None,
            spread=-4849.17,
            updated=1605295074162,
        )
        self.assertEqual(snapshots, expected)
