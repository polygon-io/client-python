from typing import Optional
from . import AssetClass, DataType
from dataclasses import dataclass


@dataclass
class SipMapping:
    CTA: Optional[str] = None
    OPRA: Optional[str] = None
    UTP: Optional[str] = None


@dataclass
class Consolidated:
    updates_high_low: Optional[bool] = None
    updates_open_close: Optional[bool] = None
    updates_volume: Optional[bool] = None

@dataclass
class MarketCenter:
    updates_high_low: Optional[bool] = None
    updates_open_close: Optional[bool] = None
    updates_volume: Optional[bool] = None


@dataclass
class UpdateRules:
    consolidated: Optional[Consolidated] = None
    market_center: Optional[MarketCenter] = None


@dataclass
class Condition:
    "Condition contains data for a condition that Polygon.io uses."
    abbreviation: Optional[str] = None
    asset_class: Optional[AssetClass] = None
    data_types: Optional[DataType] = None
    description: Optional[str] = None
    exchange: Optional[int] = None
    id: Optional[int] = None
    legacy: Optional[bool] = None
    name: Optional[str] = None
    sip_mapping: Optional[SipMapping] = None
    Type: Optional[str] = None #todo: 'type' is a keyword so here I capitalized. Should we capital case all dataclasses?
    update_rules: Optional[UpdateRules] = None

    @staticmethod
    def from_dict(d):
        return Condition(**d)
