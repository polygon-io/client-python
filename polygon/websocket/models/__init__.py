from typing import Dict, Any, List
from .common import *
from .models import *


def parse_single(data: Dict[str, Any]):
    event_type = data["ev"]
    if event_type in [EventType.EquityAgg.value, EventType.EquityAggMin.value]:
        return EquityAgg.from_dict(data)
    elif event_type == EventType.CryptoAgg.value:
        return CurrencyAgg.from_dict(data)
    elif event_type == EventType.CryptoQuote.value:
        return CurrencyAgg.from_dict(data)
    elif event_type == EventType.EquityTrade.value:
        return EquityTrade.from_dict(data)
    elif event_type == EventType.ForexTrade.value:
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
    return None


def parse(msg: List[Dict[str, Any]]) -> List[WebSocketMessage]:
    res = []
    for m in msg:
        parsed = parse_single(m)
        if parsed is None:
            if m["ev"] != "status":
                print("could not parse message", m)
        else:
            res.append(parsed)
    return res
