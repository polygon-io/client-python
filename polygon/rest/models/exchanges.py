from typing import Optional
from .common import AssetClass, Locale, ExchangeType
from dataclasses import dataclass


@dataclass
class Exchange:
    "Exchange contains data for a condition that Polygon.io uses."
    acronym: Optional[str] = None
    asset_class: Optional[AssetClass] = None
    id: Optional[int] = None
    locale: Optional[Locale] = None
    mic: Optional[str] = None
    name: Optional[str] = None
    operating_mic: Optional[str] = None
    participant_id: Optional[str] = None
    type: Optional[ExchangeType] = None
    url: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Exchange(**d)
