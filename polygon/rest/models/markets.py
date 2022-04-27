from typing import Optional
from dataclasses import dataclass


@dataclass
class Currencies:
    crypto: Optional[str] = None
    fx: Optional[str] = None


@dataclass
class Exchanges:
    nasdaq: Optional[str] = None
    nyse: Optional[str] = None
    otc: Optional[str] = None


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
    currencies: Optional[Currencies] = None
    early_hours: Optional[bool] = None
    exchanges: Optional[Exchanges] = None
    market: Optional[str] = None
    server_time: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return MarketStatus(**d)
