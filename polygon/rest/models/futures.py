from typing import Optional, List
from ...modelclass import modelclass

@modelclass
class MarketExchanges:
    "Contains exchange market status data."
    nasdaq: Optional[str] = None
    nyse: Optional[str] = None
    otc: Optional[str] = None

@modelclass
class FuturesAggregate:
    """Represents an aggregate for a futures contract."""
    close: Optional[float] = None
    dollar_volume: Optional[float] = None
    high: Optional[float] = None
    low: Optional[float] = None
    open: Optional[float] = None
    ticker: Optional[str] = None
    transaction_count: Optional[int] = None
    underlying_asset: Optional[str] = None
    volume: Optional[int] = None
    window_end: Optional[int] = None
    window_start: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return FuturesAggregate(**{k: v for k, v in d.items() if k in FuturesAggregate.__annotations__})

@modelclass
class FuturesContract:
    """Represents a futures contract."""
    active: Optional[bool] = None
    as_of: Optional[str] = None
    days_to_maturity: Optional[int] = None
    exchange_code: Optional[str] = None
    first_trade_date: Optional[str] = None
    last_trade_date: Optional[str] = None
    max_order_quantity: Optional[int] = None
    min_order_quantity: Optional[int] = None
    name: Optional[str] = None
    product_code: Optional[str] = None
    settlement_date: Optional[str] = None
    settlement_tick_size: Optional[float] = None
    spread_tick_size: Optional[float] = None
    ticker: Optional[str] = None
    trade_tick_size: Optional[float] = None
    type: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return FuturesContract(**{k: v for k, v in d.items() if k in FuturesContract.__annotations__})

@modelclass
class FuturesMarketStatus:
    """Represents the market status for a futures product."""
    exchange_code: Optional[str] = None
    market_status: Optional[str] = None
    product_code: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return FuturesMarketStatus(**{k: v for k, v in d.items() if k in FuturesMarketStatus.__annotations__})

@modelclass
class FuturesProduct:
    """Represents a futures product."""
    as_of: Optional[str] = None
    asset_class: Optional[str] = None
    asset_sub_class: Optional[str] = None
    exchange_code: Optional[str] = None
    last_updated: Optional[str] = None
    name: Optional[str] = None
    otc_eligible: Optional[bool] = None
    price_quotation: Optional[str] = None
    product_code: Optional[str] = None
    sector: Optional[str] = None
    settlement_currency_code: Optional[str] = None
    settlement_method: Optional[str] = None
    settlement_type: Optional[str] = None
    sub_sector: Optional[str] = None
    trade_currency_code: Optional[str] = None
    type: Optional[str] = None
    unit_of_measure: Optional[str] = None
    unit_of_measure_quantity: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return FuturesProduct(**{k: v for k, v in d.items() if k in FuturesProduct.__annotations__})

@modelclass
class FuturesScheduleEvent:
    """Represents a single event in a futures schedule."""
    event: Optional[str] = None
    timestamp: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return FuturesScheduleEvent(**{k: v for k, v in d.items() if k in FuturesScheduleEvent.__annotations__})

@modelclass
class FuturesSchedule:
    """Represents a futures trading schedule."""
    market_identifier_code: Optional[str] = None
    product_code: Optional[str] = None
    product_name: Optional[str] = None
    schedule: Optional[List[FuturesScheduleEvent]] = None
    session_end_date: Optional[str] = None

    @staticmethod
    def from_dict(d):
        schedule = [FuturesScheduleEvent.from_dict(e) for e in d.get("schedule", [])] if d.get("schedule") else None
        return FuturesSchedule(
            market_identifier_code=d.get("market_identifier_code"),
            product_code=d.get("product_code"),
            product_name=d.get("product_name"),
            schedule=schedule,
            session_end_date=d.get("session_end_date"),
        )

@modelclass
class FuturesQuote:
    """Represents a quote for a futures contract."""
    ask_price: Optional[float] = None
    ask_size: Optional[float] = None
    ask_timestamp: Optional[int] = None
    bid_price: Optional[float] = None
    bid_size: Optional[float] = None
    bid_timestamp: Optional[int] = None
    session_start_date: Optional[str] = None
    ticker: Optional[str] = None
    timestamp: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return FuturesQuote(**{k: v for k, v in d.items() if k in FuturesQuote.__annotations__})

@modelclass
class FuturesTrade:
    """Represents a trade for a futures contract."""
    price: Optional[float] = None
    session_start_date: Optional[str] = None
    size: Optional[float] = None
    ticker: Optional[str] = None
    timestamp: Optional[int] = None

    @staticmethod
    def from_dict(d):
        return FuturesTrade(**{k: v for k, v in d.items() if k in FuturesTrade.__annotations__})
