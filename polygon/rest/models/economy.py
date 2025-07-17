from typing import Optional
from ...modelclass import modelclass


@modelclass
class TreasuryYield:
    """
    Treasury yield data for a specific date.
    """

    date: Optional[str] = None
    yield_1_month: Optional[float] = None
    yield_3_month: Optional[float] = None
    yield_6_month: Optional[float] = None
    yield_1_year: Optional[float] = None
    yield_2_year: Optional[float] = None
    yield_3_year: Optional[float] = None
    yield_5_year: Optional[float] = None
    yield_7_year: Optional[float] = None
    yield_10_year: Optional[float] = None
    yield_20_year: Optional[float] = None
    yield_30_year: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return TreasuryYield(
            date=d.get("date"),
            yield_1_month=d.get("yield_1_month"),
            yield_3_month=d.get("yield_3_month"),
            yield_6_month=d.get("yield_6_month"),
            yield_1_year=d.get("yield_1_year"),
            yield_2_year=d.get("yield_2_year"),
            yield_3_year=d.get("yield_3_year"),
            yield_5_year=d.get("yield_5_year"),
            yield_7_year=d.get("yield_7_year"),
            yield_10_year=d.get("yield_10_year"),
            yield_20_year=d.get("yield_20_year"),
            yield_30_year=d.get("yield_30_year"),
        )


@modelclass
class FedInflation:
    cpi: Optional[float] = None
    cpi_core: Optional[float] = None
    cpi_year_over_year: Optional[float] = None
    date: Optional[str] = None
    pce: Optional[float] = None
    pce_core: Optional[float] = None
    pce_spending: Optional[float] = None

    @staticmethod
    def from_dict(d):
        return FedInflation(
            cpi=d.get("cpi"),
            cpi_core=d.get("cpi_core"),
            cpi_year_over_year=d.get("cpi_year_over_year"),
            date=d.get("date"),
            pce=d.get("pce"),
            pce_core=d.get("pce_core"),
            pce_spending=d.get("pce_spending"),
        )
