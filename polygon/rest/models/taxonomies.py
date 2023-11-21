from typing import Optional
from ...modelclass import modelclass


@modelclass
class Taxonomy:
    "Retrieve taxonomy classifications for one or more tickers."
    category: Optional[str] = None
    reason: Optional[str] = None
    relevance: Optional[float] = None
    tag: Optional[str] = None
    ticker: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Taxonomy(
            d.get("category", None),
            d.get("reason", None),
            d.get("relevance", None),
            d.get("tag", None),
            d.get("ticker", None),
        )
