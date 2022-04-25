from dataclasses import dataclass
from typing import Optional

@dataclass
class Agg:
    open: float
    high: float
    low: float
    close: float
    volume: float
    vwap: float
    timestamp: int
    transactions: int

    @staticmethod
    def from_dict(d):
        return Agg(
            d.get('o', None),
            d.get('h', None),
            d.get('l', None),
            d.get('c', None),
            d.get('v', None),
            d.get('vw', None),
            d.get('t', None),
            d.get('n', None)
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
    timestamp: int
    transactions: Optional[int]

    @staticmethod
    def from_dict(d):
        return GroupedDailyAgg(
            d.get('T', None),
            d.get('o', None),
            d.get('h', None),
            d.get('l', None),
            d.get('c', None),
            d.get('v', None),
            d.get('vw', None),
            d.get('t', None),
            d.get('n', None)
        )
