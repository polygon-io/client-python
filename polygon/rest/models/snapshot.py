from dataclasses import dataclass
from typing import Optional, List, Dict
from .aggs import Agg
from .quotes import LastQuote
from .trades import LastTrade


@dataclass
class SnapshotMin:
    "Most recent minute bar"
    accumulated_volume: Optional[float]
    open: Optional[float]
    high: Optional[float]
    low: Optional[float]
    close: Optional[float]
    volume: Optional[float]
    vwap: Optional[float]

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
    day: Optional[Agg]
    last_quote: Optional[LastQuote]
    last_trade: Optional[LastTrade]
    min: Optional[SnapshotMin]
    prev_day: Optional[Agg]
    ticker: str
    todays_change: float
    todays_change_percent: float
    updated: int

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
    change: Optional[float]
    change_percent: Optional[float]
    close: Optional[float]
    high: Optional[float]
    last_updated: Optional[int]
    low: Optional[float]
    open: Optional[float]
    previous_close: Optional[float]
    volume: Optional[float]
    vwap: Optional[float]

    @staticmethod
    def from_dict(d):
        return DayOptionContractSnapshot(**d)


@dataclass
class OptionDetails:
    contract_type: str
    exercise_style: str
    expiration_date: str
    shares_per_contract: float
    strike_price: float
    ticker: str

    @staticmethod
    def from_dict(d):
        return OptionDetails(**d)


@dataclass
class OptionLastQuote:
    ask: Optional[float]
    ask_size: Optional[float]
    bid: Optional[float]
    bid_size: Optional[float]
    last_updated: Optional[int]
    midpoint: Optional[float]
    timeframe: Optional[str]

    @staticmethod
    def from_dict(d):
        return OptionLastQuote(**d)


@dataclass
class OptionGreeks:
    delta: Optional[float]
    gamma: Optional[float]
    theta: Optional[float]
    vega: Optional[float]

    @staticmethod
    def from_dict(d):
        return OptionGreeks(**d)


@dataclass
class UnderlyingAsset:
    change_to_break_even: Optional[float]
    last_updated: Optional[int]
    price: Optional[float]
    ticker: Optional[str]
    timeframe: Optional[str]

    @staticmethod
    def from_dict(d):
        return UnderlyingAsset(**d)


@dataclass
class OptionContractSnapshot:
    break_even_price: Optional[float]
    day: Optional[Agg]
    details: Optional[OptionDetails]
    greeks: Optional[OptionGreeks]
    implied_volatility: Optional[float]
    last_quote: Optional[OptionLastQuote]
    open_interest: Optional[float]
    underlying_asset: Optional[float]

    @staticmethod
    def from_dict(d):
        return OptionContractSnapshot(**d)


@dataclass
class OrderBookQuote:
    price: Optional[float]
    exchange_shares: Dict[str, float]

    @staticmethod
    def from_dict(d):
        return OrderBookQuote(**d)


@dataclass
class SnapshotTickerFullBook:
    ticker: Optional[str]
    bids: Optional[List[OrderBookQuote]]
    asks: Optional[List[OrderBookQuote]]
    bid_count: Optional[float]
    ask_count: Optional[float]
    spread: Optional[float]
    updated: int

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
