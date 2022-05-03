from enum import Enum


class Sort(Enum):
    ASC = "asc"
    DESC = "desc"


class Order(Enum):
    ASC = "asc"
    DESC = "desc"


class Locale(Enum):
    US = "us"
    GLOBAL = "global"


class Market(Enum):
    STOCKS = "stocks"
    CRYPTO = "crypto"
    FX = "fx"


class AssetClass(Enum):
    STOCKS = "stocks"
    OPTIONS = "options"
    CRYPTO = "crypto"
    FX = "fx"


class DividendType(Enum):
    CD = "CD"
    SC = "SC"
    LT = "LT"
    ST = "ST"


class Frequency(Enum):
    ONE_TIME = 0
    ANUALLY = 1
    BIANUALLY = 2
    QUARTERLY = 4
    MONTHLY = 12


class DataType(Enum):
    DATA_TRADE = "trade"
    DATA_BBO = "bbo"
    DATA_NBBO = "nbbo"


class SIP(Enum):
    CTA = "CTA"
    UTP = "UTP"
    OPRA = "OPRA"


class ExchangeType(Enum):
    EXCHANGE = "exchange"
    TRF = "TRF"
    SIP = "SIP"


class Direction(Enum):
    GAINERS = "gainers"
    LOSERS = "losers"


class SnapshotMarketType(Enum):
    STOCKS = "stocks"
    FOREX = "forex"
    CRYPTO = "crypto"

class Timeframe(Enum):
    ANNUAL = "annual"
    QUARTERLY = "quarterly"