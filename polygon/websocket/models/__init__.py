from typing import Dict, Any, List
from .common import *
from .models import *
import logging


def parse_single(data: Dict[str, Any]):
    event_type = data["ev"]
    if event_type in [EventType.EquityAgg.value, EventType.EquityAggMin.value]:
        return EquityAgg.from_dict(data)
    elif event_type in [
        EventType.CryptoAgg.value,
        EventType.CryptoAggSec.value,
        EventType.ForexAgg.value,
        EventType.ForexAggSec.value,
    ]:
        return CurrencyAgg.from_dict(data)
    elif event_type == EventType.EquityTrade.value:
        return EquityTrade.from_dict(data)
    elif event_type == EventType.CryptoTrade.value:
        return CryptoTrade.from_dict(data)
    elif event_type == EventType.EquityQuote.value:
        return EquityQuote.from_dict(data)
    elif event_type == EventType.ForexQuote.value:
        return ForexQuote.from_dict(data)
    elif event_type == EventType.CryptoQuote.value:
        return CryptoQuote.from_dict(data)
    elif event_type == EventType.Imbalances.value:
        return Imbalance.from_dict(data)
    elif event_type == EventType.LimitUpLimitDown.value:
        return LimitUpLimitDown.from_dict(data)
    elif event_type == EventType.CryptoL2.value:
        return Level2Book.from_dict(data)
    elif event_type == EventType.Value.value:
        return IndexValue.from_dict(data)
    elif event_type == EventType.LaunchpadValue.value:
        return LaunchpadValue.from_dict(data)
    elif event_type == EventType.BusinessFairMarketValue.value:
        return FairMarketValue.from_dict(data)
    return None


def parse(msg: List[Dict[str, Any]], logger: logging.Logger) -> List[WebSocketMessage]:
    res = []
    for m in msg:
        parsed = parse_single(m)
        if parsed is None:
            if m["ev"] != "status":
                logger.warning("could not parse message %s", m)
        else:
            res.append(parsed)
    return res
