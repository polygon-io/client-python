from typing import Optional, List
from enum import Enum
from dataclasses import dataclass

class Locale(Enum):
    US = "us"
    GLOBAL = "global"

class Market(Enum):
    STOCKS = "stocks"
    CRYPTO = "crypto"
    FX = "fx"

class AssetClass(Enum):
    STOCKS = "stocks"
    OPTIONS = "options"
    CRYPTO = "crypto"
    FX = "fx"

@dataclass
class Address:
    address1: Optional[str] = None
    city: Optional[str] = None
    state: Optional[str] = None

@dataclass
class Branding:
    icon_url: Optional[str] = None
    logo_url: Optional[str] = None

@dataclass
class Publisher:
    favicon_url: Optional[str] = None
    homepage_url: Optional[str] = None
    logo_url: Optional[str] = None
    name: Optional[str] = None


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
    address: Optional[Address] = None
    branding: Optional[Branding] = None
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

    @staticmethod
    def from_dict(d):
        return TickerDetails(**d)

@dataclass
class TickerNews:
    "TickerDetails contains data for news articles relating to a stock ticker symbol."
    amp_url: Optional[str] = None
    article_url: Optional[str] = None
    author: Optional[str] = None
    description: Optional[str] = None
    id: Optional[str] = None
    image_url: Optional[str] = None
    keywords: Optional[List[str]] = None
    published_utc: Optional[str] = None
    publisher: Optional[Publisher] = None
    tickers: Optional[List[str]] = None
    title: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return TickerNews(**d)

@dataclass
class TickerTypes:
    "TickerTypes contains data ticker types."
    asset_class: Optional[AssetClass] = None
    code: Optional[str] = None
    description: Optional[str] = None
    locale: Optional[Locale] = None

    @staticmethod
    def from_dict(d):
        return TickerNews(**d)
