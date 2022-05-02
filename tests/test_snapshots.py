from polygon.rest.models import Snapshot, OptionContractSnapshot, SnapshotTickerFullBook
from base import BaseTest


class SnapshotsTest(BaseTest):
    def test_get_snapshot_all(self):
        snapshots = self.c.get_snapshot_all()
        expected = [
            Snapshot(
                day={
                    "c": 20.506,
                    "h": 20.64,
                    "l": 20.506,
                    "o": 20.64,
                    "v": 37216,
                    "vw": 20.616,
                },
                last_quote={
                    "P": 20.6,
                    "S": 22,
                    "p": 20.5,
                    "s": 13,
                    "t": 1605192959994246100,
                },
                last_trade={
                    "c": [14, 41],
                    "i": "71675577320245",
                    "p": 20.506,
                    "s": 2416,
                    "t": 1605192894630916600,
                    "x": 4,
                },
                min={
                    "av": 37216,
                    "c": 20.506,
                    "h": 20.506,
                    "l": 20.506,
                    "o": 20.506,
                    "v": 5000,
                    "vw": 20.5105,
                },
                prev_day={
                    "c": 20.63,
                    "h": 21,
                    "l": 20.5,
                    "o": 20.79,
                    "v": 292738,
                    "vw": 20.6939,
                },
                ticker="BCAT",
                todays_change=-0.124,
                todays_change_percent=None,
                updated=1605192894630916600,
            )
        ]
        self.assertEqual(snapshots, expected)

    def test_get_snapshot_direction(self):
        snapshots = self.c.get_snapshot_direction("gainers")
        expected = [
            Snapshot(
                day={
                    "c": 6.42,
                    "h": 6.99,
                    "l": 6.4,
                    "o": 6.81,
                    "v": 115782,
                    "vw": 6.656,
                },
                last_quote={
                    "P": 6.43,
                    "S": 1,
                    "p": 6.4,
                    "s": 1,
                    "t": 1651251738312628478,
                },
                last_trade={
                    "c": [14, 41],
                    "i": "100",
                    "p": 6.42,
                    "s": 200,
                    "t": 1651251334045891221,
                    "x": 8,
                },
                min={
                    "av": 115689,
                    "c": 6.42,
                    "h": 6.542,
                    "l": 6.42,
                    "o": 6.49,
                    "v": 2671,
                    "vw": 6.4604,
                },
                prev_day={
                    "c": 0.29,
                    "h": 0.348,
                    "l": 0.29,
                    "o": 0.3443,
                    "v": 1488660,
                    "vw": 0.317,
                },
                ticker="NVCN",
                todays_change=6.13,
                todays_change_percent=None,
                updated=1651251360000000000,
            ),
            Snapshot(
                day={
                    "c": 4.2107,
                    "h": 4.95,
                    "l": 4.21,
                    "o": 4.31,
                    "v": 453199,
                    "vw": 4.4181,
                },
                last_quote={
                    "P": 4.22,
                    "S": 9,
                    "p": 4.21,
                    "s": 11,
                    "t": 1651251781709136903,
                },
                last_trade={
                    "c": None,
                    "i": "1084",
                    "p": 4.2116,
                    "s": 241,
                    "t": 1651251789345841015,
                    "x": 4,
                },
                min={
                    "av": 453189,
                    "c": 4.2107,
                    "h": 4.2107,
                    "l": 4.2107,
                    "o": 4.2107,
                    "v": 1012,
                    "vw": 4.2107,
                },
                prev_day={
                    "c": 0.1953,
                    "h": 0.2966,
                    "l": 0.195,
                    "o": 0.29,
                    "v": 8784033,
                    "vw": 0.2278,
                },
                ticker="BIOL",
                todays_change=4.016,
                todays_change_percent=None,
                updated=1651251789345841015,
            ),
        ]
        self.assertEqual(snapshots, expected)

    def test_get_snapshot_ticker(self):
        snapshots = self.c.get_snapshot_ticker("AAPL")
        expected = [
            Snapshot(
                day={
                    "c": 160.315,
                    "h": 166.2,
                    "l": 159.8,
                    "o": 161.84,
                    "v": 68840127,
                    "vw": 162.7124,
                },
                last_quote={
                    "P": 159.99,
                    "S": 5,
                    "p": 159.98,
                    "s": 3,
                    "t": 1651251948407646487,
                },
                last_trade={
                    "c": None,
                    "i": "121351",
                    "p": 159.99,
                    "s": 200,
                    "t": 1651251948294080343,
                    "x": 12,
                },
                min={
                    "av": 68834255,
                    "c": 160.3,
                    "h": 160.71,
                    "l": 160.3,
                    "o": 160.71,
                    "v": 197226,
                    "vw": 160.5259,
                },
                prev_day={
                    "c": 163.64,
                    "h": 164.515,
                    "l": 158.93,
                    "o": 159.25,
                    "v": 130149192,
                    "vw": 161.8622,
                },
                ticker="AAPL",
                todays_change=-3.65,
                todays_change_percent=None,
                updated=1651251948294080343,
            )
        ]
        self.assertEqual(snapshots, expected)

    def test_get_snapshot_option(self):
        snapshots = self.c.get_snapshot_option("AAPL", "O:AAPL230616C00150000")
        expected = [
            OptionContractSnapshot(
                break_even_price=179.075,
                day={
                    "change": -2.3999999999999986,
                    "change_percent": -7.643312101910824,
                    "close": 29,
                    "high": 32.25,
                    "last_updated": 1651204800000000000,
                    "low": 29,
                    "open": 29.99,
                    "previous_close": 31.4,
                    "volume": 8,
                    "vwap": 30.7738,
                },
                details={
                    "contract_type": "call",
                    "exercise_style": "american",
                    "expiration_date": "2023-06-16",
                    "shares_per_contract": 100,
                    "strike_price": 150,
                    "ticker": "O:AAPL230616C00150000",
                },
                greeks={
                    "delta": 0.6436614934293701,
                    "gamma": 0.0061735291012820675,
                    "theta": -0.028227189324641973,
                    "vega": 0.6381159723175714,
                },
                implied_volatility=0.3570277203465058,
                last_quote={
                    "ask": 29.25,
                    "ask_size": 209,
                    "bid": 28.9,
                    "bid_size": 294,
                    "last_updated": 1651254260800059648,
                    "midpoint": 29.075,
                    "timeframe": "REAL-TIME",
                },
                open_interest=8133,
                underlying_asset={
                    "change_to_break_even": 19.11439999999999,
                    "last_updated": 1651254263172073152,
                    "price": 159.9606,
                    "ticker": "AAPL",
                    "timeframe": "REAL-TIME",
                },
            )
        ]
        self.assertEqual(snapshots, expected)

    def test_get_snapshot_crypto_book(self):
        snapshots = self.c.get_snapshot_crypto_book("X:BTCUSD")
        expected = [
            SnapshotTickerFullBook(
                ticker="X:BTCUSD",
                bids=[
                    {"p": 16303.17, "x": {"1": 2}},
                    {"p": 16302.94, "x": {"1": 0.02859424, "6": 0.023455}},
                ],
                asks=[{"p": 11454, "x": {"2": 1}}, {"p": 11455, "x": {"2": 1}}],
                bid_count=694.951789670001,
                ask_count=593.1412981600005,
                spread=-4849.17,
                updated=1605295074162,
            )
        ]
        self.assertEqual(snapshots, expected)
