from re import LOCALE
from typing import Optional, List
from models import Locale, Market
from dataclasses import dataclass


@dataclass
class Ticker:
    "Ticker contains data for a specified ticker symbol."
    active: Optional[bool] = None
    cik: Optional[str] = None
    composite_figi: Optional[str] = None
    currency_name: Optional[str] = None
    delisted_utc: Optional[str] = None
    last_updated_utc: Optional[str] = None
    locale: Optional[Locale] = None
    market: Optional[Market] = None
    name: Optional[str] = None
    primary_exchange: Optional[str] = None
    share_class_figi: Optional[str] = None
    ticker: Optional[str] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Ticker(**d)
