from typing import Optional, List
from dataclasses import dataclass


@dataclass
class Trade:
    "Trade contains trade data for a specified ticker symbol."
    conditions: Optional[List[int]] = None
    correction: Optional[int] = None
    exchange: Optional[int] = None
    id: Optional[str] = None
    participant_timestamp: Optional[int] = None
    price: Optional[float] = None
    sequence_number: Optional[int] = None
    sip_timestamp: Optional[int] = None
    size: Optional[float] = None
    tape: Optional[int] = None
    trf_id: Optional[int] = None
    trf_timestamp: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return Trade(**d)

@dataclass
class LastTrade:
    ticker: str
    trf_timestamp: int
    sequence_number: float
    sip_timestamp: int
    participant_timestamp: int
    conditions: List[int]
    correction: int
    id: str
    price: float
    trf_id: int
    size: float
    exchange: int
    tape: int

    @staticmethod
    def from_dict(d):
        return LastTrade(
            d.get("T", None),
            d.get("f", None),
            d.get("q", None),
            d.get("t", None),
            d.get("y", None),
            d.get("c", None),
            d.get("e", None),
            d.get("i", None),
            d.get("p", None),
            d.get("r", None),
            d.get("s", None),
            d.get("x", None),
            d.get("z", None),
        )