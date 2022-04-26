from typing import Optional, List
from dataclasses import dataclass


@dataclass
class Quote:
    "Quote contains quote data for a specified ticker symbol."
    ask_exchange: Optional[int] = None
    ask_price: Optional[float] = None
    ask_size: Optional[float] = None
    bid_exchange: Optional[int] = None
    bid_price: Optional[float] = None
    bid_size: Optional[float] = None
    conditions: Optional[List[int]] = None
    indicators: Optional[List[int]] = None
    participant_timestamp: Optional[int] = None
    sequence_number: Optional[int] = None
    sip_timestamp: Optional[int] = None
    tape: Optional[int] = None
    trf_timestamp: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return Quote(**d)