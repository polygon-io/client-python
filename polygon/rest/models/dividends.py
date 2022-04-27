from typing import Optional
from enum import Enum
from dataclasses import dataclass

class DividendType(Enum):
    CD = "CD"
    SC = "SC"
    LT = "LT"
    ST = "ST"

class Frequency(Enum):
    OneTime = 0
    Anually = 1
    BiAnually = 2
    Quarterly = 4
    Monthly = 12

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