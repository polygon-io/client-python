from sqlite3 import Timestamp
from typing import Optional, Any, Dict, List, Union
from ...modelclass import modelclass
from aggs import Agg

@modelclass
class IndicatorValue:
    "Contains one datum for indicators with a single value."
    timestamp: Optional[int] = None
    value: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return IndicatorValue(
            d.get("timestamp", None),
            d.get("value", None),
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
            d.get("timestamp", None),
            d.get("value", None),
            d.get("histogram", None),
            d.get("signal", None),
        )

@modelclass
class Underlying:
    "Contains one datum for all MACD values."
    url: Optional[str] = None
    aggregates: Optional[List[Agg]] = None

    @staticmethod
    def from_dict(d):
        return Underlying(
            d.get("values", None),
            d.get("underlying", None),
        )

@modelclass
class SingleIndicatorResults:
    "Contains one datum for all MACD values."
    values: Optional[List[IndicatorValue]] = None
    underlying: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return SingleIndicatorResults(
            d.get("values", None),
            d.get("underlying", None),
        )


@modelclass
class MACDIndicatorResults:
    "Contains one datum for all MACD values."
    values: Optional[List[MACDIndicatorValue]] = None
    underlying: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return MACDIndicatorResults(
            d.get("values", None),
            d.get("underlying", None),
        )