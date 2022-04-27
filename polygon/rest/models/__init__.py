from .aggs import *
from .trades import *
from .quotes import *
from .markets import *
from .tickers import *
from .splits import *
from .dividends import *

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
    OneTime = 0
    Anually = 1
    BiAnually = 2
    Quarterly = 4
    Monthly = 12
