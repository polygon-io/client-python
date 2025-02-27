from typing import Dict, Any, List, Optional
from .common import *
from .models import *
import logging

logger = logging.getLogger(__name__)


def parse_single(data: Dict[str, Any], market: Market) -> Optional[WebSocketMessage]:
    event_type = data.get("ev")
    if not event_type:
        logger.warning("No event type ('ev') found in message data")
        return None

    if market == Market.Stocks:
        if event_type == "T":
            return EquityTrade.from_dict(data)
        elif event_type == "Q":
            return EquityQuote.from_dict(data)
        elif event_type in ["A", "AM"]:
            return EquityAgg.from_dict(data)
        # Add more stock-specific events as needed (e.g., "LULD", "NOI")

    elif market == Market.Options:
        if event_type == "T":
            return OptionTrade.from_dict(data)
        elif event_type == "Q":
            return OptionQuote.from_dict(data)
        elif event_type in ["A", "AM"]:
            return OptionAggregate.from_dict(data)

    elif market == Market.Forex:
        if event_type == "C":
            return ForexQuote.from_dict(data)
        elif event_type in ["CA", "CAS"]:
            return ForexAggregate.from_dict(data)

    elif market == Market.Crypto:
        if event_type == "XT":
            return CryptoTrade.from_dict(data)
        elif event_type == "XQ":
            return CryptoQuote.from_dict(data)
        elif event_type in ["XA", "XAS"]:
            return CryptoAggregate.from_dict(data)
        elif event_type == "XL2":
            return CryptoL2Book.from_dict(data)

    elif market == Market.Indices:
        if event_type in ["A", "AM"]:
            return IndicesAggregate.from_dict(data)
        elif event_type == "V":
            return IndicesValue.from_dict(data)

    elif market == Market.Futures:
        if event_type == "T":
            return FuturesTrade.from_dict(data)
        elif event_type == "Q":
            return FuturesQuote.from_dict(data)
        elif event_type in ["A", "AM"]:
            return FuturesAggregate.from_dict(data)

    # Handle unknown markets
    else:
        logger.warning(f"Unknown market: {market}")
        return None

    # If event type is unrecognized within a known market
    logger.warning(f"Unknown event type '{event_type}' for market '{market}'")
    return None


def parse(
    msg: List[Dict[str, Any]], market: Market, logger: logging.Logger
) -> List[WebSocketMessage]:
    res = []
    for m in msg:
        parsed = parse_single(m, market)
        if parsed is None:
            if m.get("ev") != "status":
                logger.warning("could not parse message %s", m)
        else:
            res.append(parsed)
    return res
