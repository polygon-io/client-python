from dataclasses import dataclass
from typing import Optional


@dataclass
class Agg:
    open: float
    high: float
    low: float
    close: float
    volume: float
    vwap: Optional[float]
    timestamp: Optional[int]
    transactions: Optional[int]

    @staticmethod
    def from_dict(d):
        return Agg(
            d.get("o", None),
            d.get("h", None),
            d.get("l", None),
            d.get("c", None),
            d.get("v", None),
            d.get("vw", None),
            d.get("t", None),
            d.get("n", None),
        )


@dataclass
class GroupedDailyAgg:
    ticker: str
    open: float
    high: float
    low: float
    close: float
    volume: float
    vwap: Optional[float]
    timestamp: Optional[int]
    transactions: Optional[int]

    @staticmethod
    def from_dict(d):
        return GroupedDailyAgg(
            d.get("T", None),
            d.get("o", None),
            d.get("h", None),
            d.get("l", None),
            d.get("c", None),
            d.get("v", None),
            d.get("vw", None),
            d.get("t", None),
            d.get("n", None),
        )


@dataclass
class DailyOpenCloseAgg:
    after_hours: Optional[float]
    close: float
    from_: str
    high: float
    low: float
    open: float
    pre_market: Optional[float]
    status: Optional[str]
    symbol: str
    volume: float

    @staticmethod
    def from_dict(d):
        return DailyOpenCloseAgg(
            d.get("afterHours", None),
            d.get("close", None),
            d.get("from", None),
            d.get("high", None),
            d.get("low", None),
            d.get("open", None),
            d.get("preMarket", None),
            d.get("status", None),
            d.get("symbol", None),
            d.get("volume", None),
        )


@dataclass
class PreviousCloseAgg:
    ticker: str
    close: float
    high: float
    low: float
    open: float
    timestamp: Optional[float]
    volume: float
    vwap: Optional[float]

    @staticmethod
    def from_dict(d):
        return PreviousCloseAgg(
            d.get("T", None),
            d.get("c", None),
            d.get("h", None),
            d.get("l", None),
            d.get("o", None),
            d.get("t", None),
            d.get("v", None),
            d.get("vw", None),
        )
