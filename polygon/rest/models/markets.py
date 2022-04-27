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


@dataclass
class MarketStatus:
    "MarketStatus contains data for the current trading status of the exchanges and overall financial markets."
    after_hours: Optional[bool] = None
    currencies: Optional[Dict[str, str]] = None
    early_hours: Optional[bool] = None
    exchanges: Optional[Dict[str, str]] = None
    market: Optional[str] = None
    server_time: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return MarketStatus(**d)
