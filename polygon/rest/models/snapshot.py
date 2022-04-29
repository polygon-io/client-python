from dataclasses import dataclass
from typing import Optional, List, Dict
from .aggs import Agg
from .quotes import LastQuote
from .trades import LastTrade


@dataclass
class SnapshotMin:
    "Most recent minute bar"
    accumulated_volume: Optional[float] = None
    open: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    close: Optional[float] = None
    volume: Optional[float] = None
    vwap: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return SnapshotMin(
            d.get("ac", None),
            d.get("o", None),
            d.get("h", None),
            d.get("l", None),
            d.get("c", None),
            d.get("v", None),
            d.get("vw", None),
        )


@dataclass
class Snapshot:
    day: Optional[Agg] = None
    last_quote: Optional[LastQuote] = None
    last_trade: Optional[LastTrade] = None
    min: Optional[SnapshotMin] = None
    prev_day: Optional[Agg] = None
    ticker: Optional[str] = None
    todays_change: Optional[float] = None
    todays_change_percent: Optional[float] = None
    updated: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return Snapshot(
            d.get("day", None),
            d.get("lastQuote", None),
            d.get("lastTrade", None),
            d.get("min", None),
            d.get("prevDay", None),
            d.get("ticker", None),
            d.get("todaysChange", None),
            d.get("todaysChangePercent", None),
            d.get("updated", None),
        )


@dataclass
class DayOptionContractSnapshot:
    change: Optional[float] = None
    change_percent: Optional[float] = None
    close: Optional[float] = None
    high: Optional[float] = None
    last_updated: Optional[int] = None
    low: Optional[float] = None
    open: Optional[float] = None
    previous_close: Optional[float] = None
    volume: Optional[float] = None
    vwap: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return DayOptionContractSnapshot(**d)


@dataclass
class OptionDetails:
    contract_type: Optional[str] = None
    exercise_style: Optional[str] = None
    expiration_date: Optional[str] = None
    shares_per_contract: Optional[float] = None
    strike_price: Optional[float] = None
    ticker: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return OptionDetails(**d)


@dataclass
class OptionLastQuote:
    ask: Optional[float] = None
    ask_size: Optional[float] = None
    bid: Optional[float] = None
    bid_size: Optional[float] = None
    last_updated: Optional[int] = None
    midpoint: Optional[float] = None
    timeframe: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return OptionLastQuote(**d)


@dataclass
class OptionGreeks:
    delta: Optional[float] = None
    gamma: Optional[float] = None
    theta: Optional[float] = None
    vega: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return OptionGreeks(**d)


@dataclass
class UnderlyingAsset:
    change_to_break_even: Optional[float] = None
    last_updated: Optional[int] = None
    price: Optional[float] = None
    ticker: Optional[str] = None
    timeframe: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return UnderlyingAsset(**d)


@dataclass
class OptionContractSnapshot:
    break_even_price: Optional[float] = None
    day: Optional[Agg] = None
    details: Optional[OptionDetails] = None
    greeks: Optional[OptionGreeks] = None
    implied_volatility: Optional[float] = None
    last_quote: Optional[OptionLastQuote] = None
    open_interest: Optional[float] = None
    underlying_asset: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return OptionContractSnapshot(**d)


@dataclass
class OrderBookQuote:
    price: Optional[float] = None
    exchange_shares: Optional[Dict[str, float]] = None

    @staticmethod
    def from_dict(d):
        return OrderBookQuote(**d)


@dataclass
class SnapshotTickerFullBook:
    ticker: Optional[str] = None
    bids: Optional[List[OrderBookQuote]] = None
    asks: Optional[List[OrderBookQuote]] = None
    bid_count: Optional[float] = None
    ask_count: Optional[float] = None
    spread: Optional[float] = None
    updated: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return SnapshotTickerFullBook(
            d.get("ticker", None),
            d.get("bids", None),
            d.get("asks", None),
            d.get("bidCount", None),
            d.get("askCount", None),
            d.get("spread", None),
            d.get("updated", None),
        )
