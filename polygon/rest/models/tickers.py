from typing import Optional, Dict
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

@dataclass
class TickerDetails:
    "TickerDetails contains data for a specified ticker symbol."
    active: Optional[bool] = None
    address: Optional[Dict[str,str]] = None
    branding: Optional[Dict[str,str]] = None
    cik: Optional[str] = None
    composite_figi: Optional[str] = None
    currency_name: Optional[str] = None
    delisted_utc: Optional[str] = None
    description: Optional[str] = None
    homepage_url: Optional[str] = None
    list_date: Optional[str] = None
    locale: Optional[Locale] = None
    market: Optional[Market] = None
    market_cap: Optional[float] = None
    name: Optional[str] = None
    phone_number: Optional[str] = None
    primary_exchange: Optional[str] = None
    share_class_figi: Optional[str] = None
    share_class_shares_outstanding: Optional[int] = None
    sic_code: Optional[str] = None
    sic_description: Optional[str] = None
    ticker: Optional[str] = None
    total_employees: Optional[int] = None
    type: Optional[str] = None
    weighted_shares_outstanding: Optional[int] = None
