from typing import Optional
from .shared import DividendType, Frequency
from dataclasses import dataclass


@dataclass
class Dividend:
    "Dividend contains data for a historical cash dividend, including the ticker symbol, declaration date, ex-dividend date, record date, pay date, frequency, and amount."
    cash_amount: Optional[float] = None
    declaration_date: Optional[str] = None
    dividend_type: Optional[DividendType] = None
    ex_dividend_date: Optional[str] = None
    frequency: Optional[Frequency] = None
    pay_date: Optional[str] = None
    record_date: Optional[str] = None
    ticker: Optional[str] = None

    @staticmethod
    def from_dict(d):
        return Dividend(**d)
