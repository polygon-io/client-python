from typing import Dict, Any, List
from .common import *
from .models import *
import logging

# Define the mapping of market and event type to model class
MARKET_EVENT_MAP = {
    Market.Stocks: {
        "A": EquityAgg,
        "AM": EquityAgg,
        "T": EquityTrade,
        "Q": EquityQuote,
        "LULD": LimitUpLimitDown,
        "FMV": FairMarketValue,
        "NOI": Imbalance,
        "LV": LaunchpadValue,
    },
    Market.Options: {
        "A": EquityAgg,
        "AM": EquityAgg,
        "T": EquityTrade,
        "Q": EquityQuote,
        "FMV": FairMarketValue,
    },
    Market.Indices: {
        "A": EquityAgg,
        "AM": EquityAgg,
        "V": IndexValue,
    },
    Market.Futures: {
        "A": FuturesAgg,
        "AM": FuturesAgg,
        "T": FuturesTrade,
        "Q": FuturesQuote,
    },
    Market.Crypto: {
        "XA": CurrencyAgg,
        "XAS": CurrencyAgg,
        "XT": CryptoTrade,
        "XQ": CryptoQuote,
        "XL2": Level2Book,
        "FMV": FairMarketValue,
    },
    Market.Forex: {
        "CA": CurrencyAgg,
        "CAS": CurrencyAgg,
        "C": ForexQuote,
        "FMV": FairMarketValue,
    },
}


def parse_single(data: Dict[str, Any], market: Market) -> Any:
    event_type = data["ev"]
    # Look up the model class based on market and event type
    model_class = MARKET_EVENT_MAP.get(market, {}).get(event_type)
    if model_class:
        return model_class.from_dict(data)
    else:
        # Log a warning for unrecognized event types, unless it's a status message
        if event_type != "status":
            logger.warning("Unknown event type '%s' for market %s", event_type, market)
        return None


def parse(
    msg: List[Dict[str, Any]], logger: logging.Logger, market: Market
) -> List[WebSocketMessage]:
    res = []
    for m in msg:
        parsed = parse_single(m, market)
        if parsed is None:
            if m["ev"] != "status":
                logger.warning("could not parse message %s", m)
        else:
            res.append(parsed)
    return res
