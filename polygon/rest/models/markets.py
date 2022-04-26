from typing import Optional, Dict
from dataclasses import dataclass


@dataclass
class MarketHoliday:
    "MarketHoliday contains data for upcoming market holidays and their open/close times."
    close: Optional[str] = None
    date: Optional[str] = None
    exchange: Optional[str] = None
    name: Optional[str] = None
    open: Optional[str] = None
    status: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return MarketHoliday(**d)


