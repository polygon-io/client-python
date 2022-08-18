from sqlite3 import Timestamp
from typing import Optional
from ...modelclass import modelclass

@modelclass
class SingleIndicatorValue:
    "Contains one datum for indicators with a single value."
    timestamp: Optional[int] = None
    value: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return SingleIndicatorValue(
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