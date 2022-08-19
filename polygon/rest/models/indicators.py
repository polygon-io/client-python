from sqlite3 import Timestamp
from typing import Optional, Any, Dict, List, Union
from ...modelclass import modelclass
from .aggs import Agg


@modelclass
class IndicatorValue:
    "Contains one datum for indicators with a single value."
    timestamp: Optional[int] = None
    value: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return IndicatorValue(
            timestamp=d.get("timestamp", None),
            value=d.get("value", None),
        )


@modelclass
class MACDIndicatorValue:
    "Contains one datum for all MACD values."
    timestamp: Optional[int] = None
    value: Optional[float] = None
    signal: Optional[float] = None
    histogram: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return MACDIndicatorValue(
            timestamp=d.get("timestamp", None),
            value=d.get("value", None),
            signal=d.get("histogram", None),
            histogram=d.get("signal", None),
        )


@modelclass
class Underlying:
    "Contains one datum for all MACD values."
    url: Optional[str] = None
    aggregates: Optional[List[Agg]] = None

    @staticmethod
    def from_dict(d):
        return Underlying(
            url=d.get("url", None),
            aggregates=[Agg.from_dict(a) for a in d.get("aggregates", [])],
        )


@modelclass
class SingleIndicatorResults:
    "Contains one datum for all MACD values."
    values: Optional[List[IndicatorValue]] = None
    underlying: Optional[Underlying] = None

    @staticmethod
    def from_dict(d):
        return SingleIndicatorResults(
            values=[IndicatorValue.from_dict(v) for v in (d.get("values", []))],
            underlying=Underlying.from_dict(d.get("underlying", None)),
        )


@modelclass
class MACDIndicatorResults:
    "Contains one datum for all MACD values."
    values: Optional[List[MACDIndicatorValue]] = None
    underlying: Optional[Underlying] = None

    @staticmethod
    def from_dict(d):
        return MACDIndicatorResults(
            values=[MACDIndicatorValue.from_dict(v) for v in (d.get("values", []))],
            underlying=Underlying.from_dict(d.get("underlying", None)),
        )
