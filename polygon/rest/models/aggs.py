from dataclasses import dataclass
from typing import Optional

@dataclass
class Agg:
    timestamp: int
    open: float
    high: float
    low: float
    close: float
    volume: float
    vwap: Optional[float]
    transactions: Optional[int]

    @staticmethod
    def from_dict(d):
        return Agg(
                timestamp=d["t"],
                open=d["o"],
                high=d["h"], 
                low=d["l"],
                close=d["c"],
                volume=d["v"],
                vwap=d.get("vw", None),
                transactions=d.get("n", None)
        )
