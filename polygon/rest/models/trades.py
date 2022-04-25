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

