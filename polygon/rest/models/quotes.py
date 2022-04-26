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

@dataclass
class LastQuote:
    "LastQuote contains data for the most recent NBBO (Quote) tick for a given stock."
    ticker: Optional[str] = None
    trf_timestamp: Optional[int] = None
    sequence_number: Optional[int] = None
    sip_timestamp: Optional[int] = None
    participant_timestamp: Optional[int] = None
    ask_price: Optional[float] = None
    ask_size: Optional[int] = None
    ask_exchange: Optional[int] = None
    conditions: Optional[List[int]] = None
    indicators: Optional[List[int]] = None
    bid_price: Optional[float] = None
    bid_size: Optional[int] = None
    bid_exchange: Optional[int] = None
    tape: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return LastQuote(
            ticker=d.get("T", None),
            trf_timestamp=d.get("f", None),
            sequence_number=d.get("q", None),
            sip_timestamp=d.get("t", None),
            participant_timestamp=d.get("y", None),
            ask_price=d.get("P", None),
            ask_size=d.get("S", None),
            ask_exchange=d.get("X", None),
            conditions=d.get("c", None),
            indicators=d.get("i", None),
            bid_price=d.get("p", None),
            bid_size=d.get("s", None),
            bid_exchange=d.get("x", None),
            tape=d.get("z", None)
        )