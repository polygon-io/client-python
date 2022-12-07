from sqlite3 import Timestamp
from typing import Optional, Any, Dict, List, Union
from ...modelclass import modelclass
from .aggs import Agg
from .tickers import Branding

@modelclass
class Session:
    "Contains aggregate data for a given ticker symbol over a given date range in a custom time window size."
    change: Optional[float] = None
    change_percent: Optional[float] = None
    early_trading_change: Optional[float] = None
    early_trading_change_percent: Optional[float] = None
    late_trading_change: Optional[float] = None
    late_trading_change_percent: Optional[float] = None
    close: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    open: Optional[float] = None
    previous_close: Optional[float] = None
    volume: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return Session(
            d.get("change", None),
            d.get("change_percent", None),
            d.get("early_trading_change", None),
            d.get("early_trading_change_percent", None),
            d.get("late_trading_change", None),
            d.get("late_trading_change_percent", None),
            d.get("close", None),
            d.get("high", None),
            d.get("low", None),
            d.get("open", None),
            d.get("previous_close", None),
            d.get("volume", None),
        )

@modelclass
class Options:
    "Contains aggregate data for a given ticker symbol over a given date range in a custom time window size."
    contract_type: Optional[str] = None
    excercise_style: Optional[str] = None
    expiration_date: Optional[str] = None
    shares_per_contract: Optional[float] = None
    strike_price: Optional[float] = None
    underlying_ticker: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return Options(
            d.get("contract_type", None),
            d.get("excercise_style", None),
            d.get("expiration_date", None),
            d.get("shares_per_contract", None),
            d.get("strike_price", None),
            d.get("underlying_ticker", None),
        )

@modelclass
class SummaryResult:
    "Contains aggregate data for a given ticker symbol over a given date range in a custom time window size."
    price: Optional[float] = None
    name: Optional[str] = None
    ticker: Optional[str] = None
    branding: Optional[Branding] = None
    market_status: Optional[str] = None
    type: Optional[str] = None
    session: Optional[str] = None
    options: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return SummaryResult(
            price=d.get("price", None),
            name=d.get("name", None),
            ticker=d.get("ticker", None),
            branding=None 
            if "branding" not in d
            else Branding.from_dict(d['branding']),
            market_status=d.get("market_status", None),
            type=d.get("type", None),
            session=d.get("session", None),
            options=None 
            if "options" not in d
            else Options.from_dict(d['options']),
        )
        