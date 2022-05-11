from typing import Optional
from dataclasses import dataclass


@dataclass
class MarketCurrencies:
    "Contains currency market status data."
    crypto: Optional[str] = None
    fx: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return MarketCurrencies(**d)


@dataclass
class MarketExchanges:
    "Contains exchange market status data."
    nasdaq: Optional[str] = None
    nyse: Optional[str] = None
    otc: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return MarketExchanges(**d)


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
    currencies: Optional[MarketCurrencies] = None
    early_hours: Optional[bool] = None
    exchanges: Optional[MarketExchanges] = None
    market: Optional[str] = None
    server_time: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return MarketStatus(
            after_hours=d.get("after_hours", None),
            currencies=None
            if "currencies" not in d
            else MarketCurrencies.from_dict(d["currencies"]),
            early_hours=d.get("early_hours", None),
            exchanges=None
            if "exchanges" not in d
            else MarketExchanges.from_dict(d["exchanges"]),
            market=d.get("market", None),
            server_time=d.get("server_time", None),
        )
